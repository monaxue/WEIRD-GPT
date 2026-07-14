import asyncio
import pandas as pd
from survey import main

prompts = pd.read_csv("prompts/processed_prompts.csv")
#prompts = prompts.query("Name == 'core_2' or Name == 'core_1_1' ").reset_index(drop=True)

models = [
 "meta-llama/llama-4-maverick",
 "google/gemini-3.1-flash-lite",
 "openai/gpt-5.4-mini",
 "anthropic/claude-haiku-4.5",
 ]

asyncio.run(
    main(
        db_name = 'american',
        prompts=prompts, 
        iterations=90, 
        temperature=2, 
        models=models
        )
    )