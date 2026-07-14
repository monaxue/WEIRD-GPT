import pandas as pd

df1 = pd.read_excel("data/raw/gpt_3.5_wvs_data_1.xlsx")
df2 = pd.read_excel("data/raw/gpt_3.5_wvs_data_2.xlsx")


df = pd.concat([df1, df2])

df.to_excel("data/final/final_gpt_3.5_wvs_data.xlsx", index=False)