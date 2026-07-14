import asyncio
import pandas as pd
from survey import main

prompts = pd.read_csv("prompts/processed_prompts.csv")
#prompts = prompts.query("Name == 'core_2' | Name == 'core_1_1' ").reset_index(drop=True)

models = [
"deepseek/deepseek-v4-flash"
]

asyncio.run(
    main(
        db_name = 'deepseek', #chinese
        prompts=prompts, 
        iterations=80, 
        temperature=1.5, 
        models=models
        )
    )