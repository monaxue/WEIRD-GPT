import openai
import time
import numpy as np
import os
import pandas as pd

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Number of runs per randomized permutation
n=1

# some parameters
model_engine = "text-davinci-003"
iterations = 842
count=0

# import questions/parameters from the questions python file
import values_questions
survey_items_names = values_questions.survey_items_names
number_of_items = values_questions.number_of_items
survey_items = values_questions.survey_items
df = values_questions.df_i.copy()

# File for history
file = open("values_history.txt", "a")

# Run ths study
while count < iterations:
    
    perm_item=np.random.permutation(number_of_items)
    i = 0
    for i in range(number_of_items):
        perm_subitem=np.random.permutation(len(survey_items[perm_item[i]]))
        j = 0
        while j < len(survey_items[perm_item[i]]):
            try:    
                item_name = survey_items_names[perm_item[i]][perm_subitem[j]]
                item=survey_items[perm_item[i]][perm_subitem[j]]
                response = openai.Completion.create(
                    model=model_engine,
                    prompt=str(item) 
                    
                    + " Please only answer with a single number." ## For answers that only have one number to report (instead of a list of numbers or other answers).
                    
                    #+ " Please, do not use commas or and to separate out different answers. Instead, put each answer on a separate line in a enumerated list in the form. For instance, each line should first have the line number, followed by a period, followed by a space, then followed by the answer." ## For questions that come in a list form.
                    ,
                    max_tokens=2048,
                    #Number of attempts per randomized permutation
                    n=n,
                    stop=None,
                    temperature=1.0
                )
                answers_list = response.choices[0].text.split('\n')[2:]
                # answers_list = [answer for answer in response.choices[0].text.split('\n') if answer != ""]
                if len(answers_list) > 1:
                    item_name_actual = [None] * len(answers_list)
                    for subno in range(len(answers_list)):
                        item_name_actual[subno] = str(item_name) + "_" + str(subno+1)
                else:
                    item_name_actual = [item_name]
                answers = 'Iteration '+str(count)+ "\n" + str(response.choices[0].text) + "\n" +str(item_name_actual) + "\n" +str(answers_list) + "\n\n"
                print(answers)
                file.write(answers)
                for c in range(len(answers_list)):
                    df.loc[count, item_name_actual[c]] = answers_list[c]
                #time.sleep(5)
                j+=1
            except Exception as e:
                item_name = survey_items_names[perm_item[i]][perm_subitem[j]]
                error_message = str(item_name) + "\nError, trying again in 60 seconds\n" + str(e) + "\n"
                print(error_message) 
                file.write(error_message)
                time.sleep(60)
    count +=1
        

    

print(df)

df.to_excel('values_qs_3.xlsx', index=False)


## If answers come in a numerical list, use the following code

# df = pd.read_excel('values_qs.xlsx')

# def remove_number(answer):
#     first_period_ind = answer.find('.')
#     return answer[first_period_ind + 1::].strip() 

# df_num_removed = df.copy().astype(str).applymap(remove_number)

# df_num_removed.to_excel('values_qs_num_removed.xlsx', index=False)




