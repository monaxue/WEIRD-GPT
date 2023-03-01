import pandas as pd

df0 = pd.read_excel('data/cleaned_data/processed/cleaned_values_qs_0.xlsx')
df1 = pd.read_excel('data/cleaned_data/processed/cleaned_values_qs_1.xlsx')
df2 = pd.read_excel('data/cleaned_data/processed/cleaned_values_qs_2.xlsx')
df3 = pd.read_excel('data/cleaned_data/processed/cleaned_values_qs_3.xlsx')

df = pd.concat([df0,df1,df2,df3])

df.to_excel('data/cleaned_data/final/final_cleaned_values_qs.xlsx', index=False)