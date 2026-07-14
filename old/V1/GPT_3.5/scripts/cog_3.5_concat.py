import pandas as pd

df3 = pd.read_excel('gpt_3.5_cognitive_new_3.xlsx')
df4 = pd.read_excel('gpt_3.5_cognitive_new_4.xlsx')
df5 = pd.read_excel('gpt_3.5_cognitive_new_5.xlsx')
df6 = pd.read_excel('gpt_3.5_cognitive_new_6.xlsx')
df7 = pd.read_excel('gpt_3.5_cognitive_new_7.xlsx')
df8 = pd.read_excel('gpt_3.5_cognitive_new_8.xlsx')
df9 = pd.read_excel('gpt_3.5_cognitive_new_9.xlsx')


df = pd.concat([df3, df4, df5, df6[:len(df6)-1], df7, df8[:len(df8)-1], df9])

df.to_excel('final_3.5_cognitive_new.xlsx', index=False)