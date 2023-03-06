import openai
import time
import numpy as np
import os
import pandas as pd
import pickle

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#output files
output_df = "gpt_3.5_cognitive_test.xlsx"

# File for history
history_file = open("cognitive_history_3.5_test.txt", "a")
all_answer_file = open('all_answers_cognitive_3.5_test.pickle', 'ab')

# some parameters
model_engine = "gpt-3.5-turbo"
iterations = 3
count=0
n = 1

# import questions/parameters from the questions python file
import cognitive_questions_2
survey_items_names = cognitive_questions_2.survey_items_names
number_of_items = cognitive_questions_2.number_of_items
survey_items = cognitive_questions_2.survey_items
df = cognitive_questions_2.df_i.copy()

class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answer_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answer_list = answer_list


# Run ths study
while count < iterations:
    
    perm_item=np.random.permutation(number_of_items)
    i = 0
    for i in range(number_of_items):
        perm_subitem=np.random.permutation(len(survey_items[perm_item[i]]))
        j = 0
        while j < len(survey_items[perm_item[i]]):
            try:    
                master_name = survey_items_names[perm_item[i]][perm_subitem[j]]
                item=survey_items[perm_item[i]][perm_subitem[j]]

                response = openai.ChatCompletion.create(
                    model=model_engine,
                    messages=[{"role": "user", "content": str(item) 
                    
                    #+ " Please only answer with a single number." ## For answers that only have one number to report (instead of a list of numbers or other answers).
                    
                    + " Please, do not use commas or and to separate out different answers. Instead, put each answer on a separate line in a enumerated list in the form. For instance, each line should first have the line number, followed by a period, followed by a space, then followed by the answer." ## For questions that come in a list form.
                    }]
                    ,
                    max_tokens=2048,
                    #Number of attempts per randomized permutation
                    n=n,
                    stop=None,
                    temperature=1.0
                )
                answers_list = [answer for answer in response['choices'][0]['message']['content'].split('\n') if answer != ""]
                if len(answers_list) > 1:
                    names_list = [None] * len(answers_list)
                    names_list = [str(master_name) + "_" + str(sub_num+1) for sub_num in range(len(answers_list))]
                else:
                    names_list = [master_name]

                answer = Answer(iteration = count, master_name = master_name, names_list = names_list, full_answer = response['choices'][0]['message']['content'], answer_list = answers_list)
                pickle.dump(answer, all_answer_file)

                for c in range(len(answers_list)):
                    df.loc[count, names_list[c]] = answers_list[c]
                df.to_excel(output_df, index=False)
                
                success_message = 'Iteration: '+str(count) + "\nMaster_name: " + str(master_name) + "\nSuccess" +"\n" #+ "\nNames_list: " + str(names_list) + "\nAnswers_list: " + str(answers_list) + "\n"
                print(success_message)
                history_file.write(success_message)

                #time.sleep(5)
                j+=1
            except Exception as e:
                master_name = survey_items_names[perm_item[i]][perm_subitem[j]]
                error_message = 'Iteration: ' + str(count) + '\nMaster_name: ' + str(master_name) + "\nError, trying again in 60 seconds\n" + str(e) + "\n"
                print(error_message) 
                history_file.write(error_message)
                time.sleep(60)
                
    count +=1
        
history_file.close
all_answer_file.close

## make dataframe from all_answers
# for answer in all_answers:
#     df.loc[answer.iteration, answer.names_list] = answer.answers_list
# 
# df.to_excel('gpt_3.5_values_qs_1.xlsx', index=False)


## If answers come in a numerical list, use the following code

# df = pd.read_excel('values_qs.xlsx')

# def remove_number(answer):
#     first_period_ind = answer.find('.')
#     return answer[first_period_ind + 1::].strip() 

# df_num_removed = df.copy().astype(str).applymap(remove_number)

# df_num_removed.to_excel('values_qs_num_removed.xlsx', index=False)




