# This is the most up-to-date, async/parallel version of the script to run the survey. This script includes the functions. Running the functions are in separate files.

import os
from sqlalchemy import Column, Integer, String, Numeric, text
from sqlalchemy.orm import DeclarativeBase
from pydantic_ai import Agent
from pydantic import BaseModel, ValidationInfo, field_validator
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
from pydantic_ai.settings import ModelSettings
from pydantic_ai.output import PromptedOutput
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
load_dotenv(override=True)
import asyncio
import time
import logging
import uuid
import json

logging.basicConfig(level=logging.INFO, format='%(message)s')
logging.getLogger("httpx").setLevel(logging.WARNING)


# CREATE SQL DATABASE

class Base(DeclarativeBase):
    pass

class DataTable(Base):
    __tablename__="data"
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
    run_id = Column(String)
    id = Column(String)
    model = Column(String)
    name = Column(String)
    prompt = Column(String)
    instructions = Column(String)
    thinking = Column(String)
    full_answer = Column(String)
    answer = Column(String)
    input_tokens = Column(Integer)
    output_tokens = Column(Integer)
    requests = Column(Integer)
    temperature = Column(Numeric)
    time = Column(String)
    error = Column(String)


# FUNCTIONS

class IntList(BaseModel):
    answer: list[int]
    @field_validator('answer')
    @classmethod
    def is_in_range(cls, v: list[int], info: ValidationInfo) -> list[int]:
        integers = set(map(int, info.context.get('integers', '').split(','))) if info.context.get('integers', '') else set()
        lengths = set(map(int, info.context.get('lengths', '').split(','))) if info.context.get('lengths', '') else set()
        disallowed_integers = set(v) - integers
        disallowed_lengths = {len(v)} - lengths
        if len(disallowed_lengths) > 0 or len(disallowed_integers) > 0:
            if len(disallowed_integers) > 0:
                raise ValueError(
                    f'\nThe answer contains {disallowed_integers} '
                    f'when only {integers} are allowed.')
            if len(disallowed_lengths) > 0:
                raise ValueError(
                    f'\nThe answer has length {len(v)} '
                    f'when it should one of the following lengths: {disallowed_lengths}.')
        return v




async def main(iterations, prompts, models, temperature, sleep=30, rate_limit = 0, sem=15, max_rounds = 5, db_name='data'):

    os.makedirs('data/raw', exist_ok=True)
    engine = create_engine('sqlite:///data/raw/' + str(db_name) + '.db')
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        conn.execute(text("PRAGMA journal_mode=WAL"))
        conn.commit()

    Session = sessionmaker(engine)
    
    run_id = str(uuid.uuid4())
    model_last_call = {}
    sem = asyncio.Semaphore(sem)
    rate_lock = asyncio.Lock()

    pending = [(m, i, p)
    for m in models
    for i in range(iterations)
    for p in range(len(prompts))
    ]

    no_progress_rounds = 0
    last_failed = None

    round = 0

    while pending:
        round += 1

        tasks = [run_survey(iterations = iterations, 
        i = i, 
        prompts = prompts, 
        p = p, 
        m = m, 
        temperature = temperature, 
        rate_limit = rate_limit, 
        sem = sem, 
        model_last_call=model_last_call,
        rate_lock=rate_lock,
        run_id=run_id,
        Session=Session) 
        for m, i, p in pending
        ]
    
        results = await asyncio.gather(*tasks, return_exceptions=True)

        failed = []
        for (m, i, p), result in zip(pending, results):
            if isinstance(result, Exception):
                failed.append((m, i, p))
        
        if last_failed is not None and set(failed) == last_failed:
            no_progress_rounds +=1
        else:
            no_progress_rounds = 0
        
        last_failed = set(failed)

        if no_progress_rounds > 0:
            no_progress_message = ("No progress: " + str(no_progress_rounds) + "/" + str(max_rounds) + "\n\n")
            logging.info(no_progress_message)

        if no_progress_rounds >= max_rounds:
            stop_message = ("Stopping: " + str(len(failed)) + " consistently failed for " + str(max_rounds) +  " rounds\n\n")
            logging.info(stop_message)
            break 
        
        pending = failed        
        if pending:
            await asyncio.sleep(sleep)
    
    total_tasks = len(models) * iterations * len(prompts)
    completed = total_tasks - len(pending)
    logging.info(f"\nScript finished. Completed: {completed}/{total_tasks}. Remaining failed tasks: {len(pending)}\n")
            

async def run_survey(iterations, i, prompts, p, m, temperature, rate_limit, sem, model_last_call, rate_lock, run_id, Session):
    
    if rate_limit > 0:
        async with rate_lock: 
            total_wait = 60/rate_limit 
            last = model_last_call.get(m,0)
            time_since_last = (time.time() - last)
            wait = total_wait - time_since_last
            model_last_call[m] = time.time()
        if wait > 0:
            await asyncio.sleep(wait)
        
    
    async with sem:
        error = ""
        name=str(prompts.loc[p, "Name"])
        instructions = prompts.loc[p,"Instructions"]
        prompt = str(prompts.loc[p, "Prompt"])
        temperature = round(float(temperature), 1)

        model = OpenRouterModel(m, provider=
            OpenRouterProvider(api_key=os.getenv("OPENROUTER_API_KEY")))

        try:
            agent = Agent(model=model, 
                output_type=IntList, 
                instructions=instructions, 
                output_retries=3,
                model_settings=ModelSettings(temperature=temperature),
                validation_context={"integers": prompts.loc[p, "ValidIntegers"], 
                "lengths": prompts.loc[p, "ValidLengths"]})
            result = await agent.run(prompt)
        except Exception:
            try: 
                agent = Agent(model=model, 
                    output_type=PromptedOutput(IntList), 
                    instructions=instructions, 
                    output_retries=3,
                    model_settings=ModelSettings(temperature=temperature),
                    validation_context={"integers": prompts.loc[p, "ValidIntegers"], 
                    "lengths": prompts.loc[p, "ValidLengths"]})
                result = await agent.run(prompt)  
            except Exception as e:
                error = error + "\n" + str(e)
                status = ("\nAPI call failed" + "\nError messages: " + error)
                message = (
                    "Time: " + str(time.time()) +
                    '\nModel: ' + m + 
                    '\nIteration: ' + str(i+1) + '/' + str(iterations) + 
                    "\nPrompt name: " + name + 
                    status + "\n\n")
                logging.info(message)
                raise

        try: 
            answer=json.dumps(result.output.answer)
        except Exception as e:
            answer = None
            error = error + "\n" + str(e)

        try:
            full_answer = str(result.all_messages()[1].parts[1].args)
            thinking=str(result.all_messages()[1].parts[0].content)
        except Exception:
            try:
                full_answer = str(result.all_messages()[1].parts[1].content)
                thinking=str(result.all_messages()[1].parts[0].content)
            except Exception:
                    try:
                        full_answer = str(result.all_messages()[1].parts[1])
                        thinking = str(result.all_messages()[1].parts[0].content)
                    except Exception:
                        try: 
                            full_answer = str(result.all_messages()[1].parts[1])
                            thinking = str(result.all_messages()[1].parts[0])
                        except Exception:
                            try:
                                full_answer = str(result.all_messages()[1].parts[0].args)
                                thinking = "None"
                            except Exception:
                                try:
                                    full_answer = str(result.all_messages()[1].parts[0].content)
                                    thinking = "None"
                                except Exception:
                                    try:
                                        full_answer = str(result.all_messages()[1].parts[0])
                                        thinking = "None"
                                    except Exception as e:
                                        full_answer = None
                                        thinking = "None"
                                        error = error + "\n" + str(e)

        try:
            input_tokens = result.usage().input_tokens
        except Exception as e:
            input_tokens = None
            error = error + "\n" + str(e)

        try:       
            output_tokens = result.usage().output_tokens
        except Exception as e:
            output_tokens = None
            error = error + "\n" + str(e)

        try:
            requests = result.usage().requests
        except Exception as e:
            requests = None
            error = error + "\n" + str(e)

        for attempt in range(10):
            try:
                with Session() as session:

                    data = DataTable(
                        id=str(prompts.loc[p,"Original_ID"]),
                        run_id = run_id,
                        name=name, 
                        model = m,
                        prompt=prompt, 
                        instructions=instructions, 
                        thinking=thinking,
                        full_answer = full_answer,
                        answer=answer,
                        input_tokens = input_tokens,
                        output_tokens = output_tokens,
                        requests = requests,
                        temperature = temperature,
                        time = str(time.time()),
                        error = error if error else None
                        )
                    session.add(data)
                    session.commit()

                    if error == "":
                        status = "\nSuccess"
                    else:
                        status= ("\n Partial success" + "\nError messages: " + error)

                    message = (
                        "Time: " + str(time.time()) +
                        '\nModel: ' + m + 
                        '\nIteration: ' + str(i+1) + '/' + str(iterations) + 
                        "\nPrompt name: " + name + 
                        status + "\n\n")
                
                    logging.info(message)

                    break

            except Exception as e:
                if attempt < 9:
                    await asyncio.sleep(1)
                    continue
                else:
                    error = error + "\n" + str(e)
                    status = ("\nDB write failed" + "\nError messages: " + error + "\nAttempting to save to JSON")
                    message = (
                        "Time: " + str(time.time()) +
                        '\nModel: ' + m + 
                        '\nIteration: ' + str(i+1) + '/' + str(iterations) + 
                        "\nPrompt name: " + name + 
                        status + "\n\n")
                    logging.info(message)
                    try:
                        os.makedirs('data/failed_writes', exist_ok=True)
                        with open(f"data/failed_writes/{run_id}_{name}_{uuid.uuid4()}.json", "w") as f:
                            f.write(str([msg for msg in result.all_messages()]))

                        if error == "":
                            status = "\nSuccess"
                        else:
                            status= ("\n JSON write successful" + "\nError messages: " + error)

                        message = (
                            "Time: " + str(time.time()) +
                            '\nModel: ' + m + 
                            '\nIteration: ' + str(i+1) + '/' + str(iterations) + 
                            "\nPrompt name: " + name + 
                            status + "\n\n")
                
                        logging.info(message)
                        
                    except Exception as e:
                        logging.info("\nFailed to save to JSON" + "\nError Message: " + str(e))
                        raise