import pandas as pd

# If answers come in a numerical list, use the following code

df = pd.read_excel('data/cleaned_data/manual_cleaned_cognitive_qs.xlsx')

def remove_number(answer):
    first_period_ind = answer.find('.')
    return answer[first_period_ind + 1::].strip() 

df_num_removed = df.copy().astype(str).applymap(remove_number)

df_num_removed.to_excel('data/cleaned_data/manual_cleaned_cognitive_qs_num_removed.xlsx', index=False)