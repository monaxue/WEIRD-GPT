## This is the sequential (old) version. Please use async.py

import os
from sqlalchemy import Column, Integer, String, Numeric, text
from sqlalchemy.orm import DeclarativeBase
from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel
from pydantic_ai.providers.openrouter import OpenRouterProvider
from pydantic_ai.settings import ModelSettings
from sqlalchemy import create_engine
import ast
import pandas as pd
from sqlalchemy.orm import sessionmaker
import time
from dotenv import load_dotenv
load_dotenv(override=True)

# Create SQL database #

class Base(DeclarativeBase):
    pass

class DataTable(Base):
    __tablename__="data"
    unique_id = Column(Integer, primary_key=True, autoincrement=True)
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

engine = create_engine('sqlite:///data/data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(engine)


# Load prompts #

prompts = pd.read_csv("prompts/processed_prompts.csv")

# Config #

# prompts = prompts.query("Name == 'core_2' ").reset_index(drop=True) # to filter for certain questions

iterations = 1

temperature = 2

models = [
    "minimax/minimax-m2.5:free",
    #"nvidia/nemotron-3-super-120b-a12b:free",
    #"z-ai/glm-5",
    #"moonshotai/kimi-k2.5",
    #"qwen/qwen3.5-plus-20260420",
    #"anthropic/claude-opus-4.7",
    #"google/gemini-3.1-pro-preview",
    #"openai/gpt-5.5",
    #"deepseek/deepseek-v4-pro",
    #"meta-llama/llama-4-maverick",
]#

# Run survey #

for m in models:

    model = OpenRouterModel(
    m, 
    provider=OpenRouterProvider(api_key=os.getenv("OPENROUTER_API_KEY")))

    i = 0

    while i < iterations:

        p = 0

        while p < prompts.shape[0]:
            
            try:
                name=str(prompts.loc[p, "Name"])
                instructions = prompts.loc[p,"Instructions"]
                prompt = str(prompts.loc[p, "Prompt"])
                agent = Agent(model=model, 
                output_type=list[int], 
                instructions=instructions, 
                model_settings=ModelSettings(temperature=temperature))

                result = agent.run_sync(prompt)

                with Session() as session:
                    data = DataTable(
                        id=str(prompts.loc[p,"Original_ID"]),
                        name=name, 
                        model = m,
                        prompt=str(result.all_messages()[0].parts[0].content), 
                        instructions=str(result.all_messages()[0].instructions), 
                        thinking=str(result.all_messages()[1].parts[0].content),
                        full_answer = str(result.all_messages()[1].parts[1].args),
                        answer=str(result.output),
                        input_tokens = result.usage().input_tokens,
                        output_tokens = result.usage().output_tokens,
                        requests = result.usage().requests,
                        temperature = temperature)

                    session.add(data)
                    session.commit()

                success_message = 'Model: ' + m + '\nIteration: '+str(i) + "\nPrompt name: " + name + "\nSuccess" +"\n"

                print(success_message)

                p+=1
            except Exception as e:
                t = 30
                error_message = 'Model: ' + m + '\nIteration: ' + str(i) + '\nPrompt name: ' + str(prompts.loc[p, "Name"]) + "\nError, trying again in " + t + " seconds\n" + str(e) + "\n"
                print(error_message) 
                time.sleep(t)       
        i +=1
