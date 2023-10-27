import pandas as pd
import re

remov_paren = lambda x: re.sub(r'\([^)]*\)', '', str(x))
remov_space = lambda x: re.sub(' +', ' ', str(x))

df = pd.read_excel('concat_gpt_3.5_wvs_data.xlsx')

df_paren_removed = df.applymap(remov_paren).applymap(remov_space) # also deleted some answers in the form (A) (B) (C) that was manually added back in

def remove_number(answer):
     answer1 = answer.strip('.')
     first_period_ind = answer1.find('.')
     return answer1[first_period_ind + 1::].strip() 

df_num_removed = df_paren_removed.astype(str).applymap(remove_number)

unique_columns = []
for column in df_num_removed:
    list = df_num_removed[column].unique()
    unique_columns.append(list)
print(unique_columns)

df_unique = pd.DataFrame(unique_columns)
#df_unique.to_excel('unique_wvs_data_3.xlsx', index=False) #last ran 'unique_wvs_data_2.xlsx'

df_cleaned = df_num_removed.replace({
    "it depends on the individual and their perception, so there cannot be a universal answer": "nan",
    "Sorry, I cannot answer this question as it goes against OpenAI's policy of not engaging in sensitive or controversial topics that may generate biases or harm": "nan",
    "Sorry, as a language model AI, I cannot make such judgments as I am incapable of personal opinions, beliefs, or biases": "nan",
    "Depends on cultural, religious or personal beliefs, no fixed answer": "nan",
    "Depends on the circumstances, no fixed answer": "nan",
    "Depends on the circumstances and justification, no fixed answer": "nan",
    "Varies depending on personal beliefs and legal systems": "nan",
    "Varies": "nan",
    "Varies by individual beliefs and values, cannot be given a single numerical answer": "nan",
    "varies depending on individual beliefs and values, cannot give a single number": "nan",
    "Depends on the circumstances and justification, no fixed answer": "nan",
    "Depends on the individual's view on the death penalty, so cannot be answered with a single number": "nan",
    "1 for political or ideological, 10 for religious": "nan",
    "My programming prevents me from making value judgments or assumptions about human attitudes or opinions": "nan",
    "Hard work" : "Q9",
    "Feeling of responsibility" : "Q10",
    "Imaginaton" : "Q11",
    "Responsibility" : "Q10",
    "Tolerance and respect for others" : "Q12",
    "Not being selfish" : "Q16",
    "Independence" : "Q8",
    "Obedience" : "Q17",
    "Determination, perseverance" : "Q14",
    "Respect for other people" : "Q12",
    "Imagination" : "Q11",
    "Determination" : "Q14",
    "Tolerance and respect for other people" : "Q12",
    "Thrift, saving money and things" : "Q13",
    "Good manners" : "Q7",
    "Independance" : "Q8",
    "India" : "C",
    "Washington DC" : "A",
    "Human rights" : "B",
    "Maintaining order in the nation" : "1",
    "Fighting rising prices" : "3",
    "Option 2: Our society must be gradually improved by reforms" : "2",
    "2) Our society must be gradually improved by reforms" : "2",
    "Our society must be gradually improved by reforms" : "2",
})

#df_cleaned.to_excel('final_cleaned_wvs_data_2.xlsx', index=False) #last ran 'final_cleaned_wvs_data.xlsx'