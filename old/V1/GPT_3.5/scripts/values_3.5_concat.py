import pandas as pd

df2 = pd.read_excel('gpt_3.5_values_1.xlsx')
df3 = pd.read_excel('gpt_3.5_values_2.xlsx')



df = pd.concat([df2, df3])

df.to_excel('final_3.5_values.xlsx', index=False)