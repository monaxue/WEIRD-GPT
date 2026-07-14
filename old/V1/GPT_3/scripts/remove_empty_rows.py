import pandas as pd

df = pd.read_excel('values_qs_old.xlsx')

df = pd.DataFrame.dropna(df)

df.to_excel('values_qs_0.xlsx', index=False)