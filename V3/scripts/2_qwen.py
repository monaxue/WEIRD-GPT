import asyncio
import pandas as pd
from survey import main

prompts = pd.read_csv("prompts/processed_prompts.csv")
#prompts = prompts.query("Name == 'core_2' | Name == 'core_1_1' ").reset_index(drop=True)

models = [
"qwen/qwen3.5-flash-02-23",
]

asyncio.run(
    main(
        db_name = 'qwen',
        prompts=prompts, 
        iterations=80, 
        temperature=1.5, 
        models=models
        )
    )