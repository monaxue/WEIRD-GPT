import sqlite3
import pandas as pd
import glob


all_data = []
files = glob.glob('data/raw/*.db')


standard_columns = [
        'unique_id', 'run_id', 'id', 'model', 'name', 'prompt', 
        'instructions', 'thinking', 'full_answer', 'answer', 
        'input_tokens', 'output_tokens', 'requests', 'temperature', 
        'time', 'run_number', 'error'
    ]

for file in files:
    try:
        with sqlite3.connect(file) as conn: 
            df = pd.read_sql_query("SELECT * FROM data", conn)

            for col in standard_columns:
                if col not in df.columns:
                    df[col] = None

            df = df[[col for col in standard_columns]]
            all_data.append(df)

    except Exception as e:
        print(str(e))
            
merged = pd.concat(all_data, ignore_index=True)
merged['unique_id'] = range(1, len(merged) + 1)
merged.to_csv('raw/data/full_dataset.csv', index=False)

