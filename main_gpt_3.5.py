import openai
import time
import numpy as np
import os
import pandas as pd
import pickle

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#output files
output_df = "gpt_3.5_additional_values_data_1.xlsx"

# File for history
history_file = open("gpt_3.5_additional_values_history_1.txt", "a")
all_answers_file = open('gpt_3.5_additional_values_data_1.pickle', 'ab')

# some parameters
model_engine = "gpt-3.5-turbo-0301"
iterations = 1000
count=0
n = 1

# import questions/parameters from the questions python file
import additional_values_questions
survey_items_names = additional_values_questions.survey_items_names
number_of_items = additional_values_questions.number_of_items
survey_items = additional_values_questions.survey_items
df = additional_values_questions.df_i.copy()

# Create class for storing all the data in a easy to manipuate format in the future. The data is eventually stored in  pickle file.
class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answers_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answers_list = answers_list

# For cognitive tasks: function for matching question answers to questions names according to list number
def sub_numb(answer):
    period_ind = answer[:5].find('.')
    first_ind = period_ind
    colon_ind = answer[:5].find(':')
    dash_ind = answer[:5].find('-')
    first_ind = min((ind for ind in [period_ind, colon_ind, dash_ind] if ind != -1), default=-1)
    
    if first_ind == -1:  # period, colon, and dash not found in the first 5 characters
        return 'na'
    else:
        return answer[:first_ind].strip()

# For values survey: fuctions for removing extra words after the numerical answer    
def remove_extra(answer):
    period_ind = answer[:5].find('.')
    colon_ind = answer[:5].find(':')
    dash_ind = answer[:5].find('-')
    paren_ind = answer[:5].find('(')
    first_ind = min((ind for ind in [period_ind, colon_ind, dash_ind, paren_ind] if ind != -1), default=-1)
    
    if first_ind == -1:  # period, colon, and dash not found in the first 5 characters
        return answer.strip()
    else:
        return answer[:first_ind].strip()

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
                    
                    ## For answers that only have one number to report (instead of a list of numbers or other answers).
                    #+ " Please only answer with a single number." 
                    
                    ## For questions that come in a list form.
                    #+ "Please, do not use commas or 'and' to separate out different answers. And please do not lump answers together. For instance, if multiple answers fall under 'irrelevant', do not answer like to following or similar formats: '20, 21, 22 - irrelevant to establishing motive.' Instead, put each answer on a separate line in a enumerated list in the form. For instance, each line should first have the line number, followed by a period, followed by a space, then followed by the answer. So for the above example, you would have: \n20. Irrelevant. \n21. Irrelevant. \n22 Irrelevant." 
                    }]
                    ,
                    max_tokens=2048,
                    #Number of attempts per randomized permutation
                    n=n,
                    stop=None,
                    temperature=1.0
                )
                ## answer list for cognitive task
                #answers_list = [answer for answer in response['choices'][0]['message']['content'].split('\n') if answer != ""]
                
                ## asnwer list for values survey
                answers_list = [remove_extra(answer) for answer in response['choices'][0]['message']['content'].split('\n') if answer != ""]
                
                if len(answers_list) > 1:
                    names_list = [None] * len(answers_list)

                    ##values
                    names_list = [str(master_name) + "_" + str(sub_num+1) for sub_num in range(len(answers_list))] 

                    ##cognitive
                    #names_list = [str(master_name) + "_" + str(sub_numb(answer)) for answer in answers_list] 
                else:
                    names_list = [master_name]

                answer = Answer(iteration = count, master_name = master_name, names_list = names_list, full_answer = response['choices'][0]['message']['content'], answers_list = answers_list)
                pickle.dump(answer, all_answers_file)
                all_answers_file.flush()
                
                df.loc[count, names_list] = answers_list
                df.to_excel(output_df, index=False)
                
                success_message = 'Iteration: '+str(count) + "\nMaster_name: " + str(master_name) + "\nSuccess" +"\n" #+ "\nNames_list: " + str(names_list) + "\nAnswers_list: " + str(answers_list) + "\n"
                print(success_message)
                history_file.write(success_message)
                history_file.flush()

                #time.sleep(5)
                j+=1
            except Exception as e:
                master_name = survey_items_names[perm_item[i]][perm_subitem[j]]
                error_message = 'Iteration: ' + str(count) + '\nMaster_name: ' + str(master_name) + "\nError, trying again in 60 seconds\n" + str(e) + "\n"
                print(error_message) 
                history_file.write(error_message)
                history_file.flush()
                time.sleep(60)
                
    count +=1
        
history_file.close
all_answers_file.close

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




