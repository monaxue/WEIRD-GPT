import openai
import time
import numpy as np
import os
import pandas as pd
import pickle
import time

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answers_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answers_list = answers_list

def create_names(master_name, answers_list):
    names_list = []
    for answer in answers_list:
        period_ind = answer[:5].find('.')
        first_ind = period_ind
        colon_ind = answer[:5].find(':')
        dash_ind = answer[:5].find('-')
        first_ind = min((ind for ind in [period_ind, colon_ind, dash_ind] if ind != -1), default=-1)
    
        if first_ind == -1:  # period, colon, and dash not found in the first 5 characters
            name = str(master_name) + "_" + 'na_' + str(answers_list.index(answer))
        else:
            name = str(master_name) + "_" + answer[:first_ind].strip()
        names_list.append(name)
    return names_list


master_name = "happiness_5"
question = "How satisfied is an average human with the financial situation of their household? Please respond on a scale of 1 to 10, where 1 means they are “completely dissatisfied” and 10 means they are “completely satisfied.” Where would an average human put their satisfaction with their financial situation of their household?  I know that you don't have access to empirical data on this question, just provide your best estimate. Please only answer with a single number, with no additional explanation. Do not use any words to justify your answer."

df = pd.DataFrame(columns= ['happiness_5'])

output_df = "gpt_3.5_happiness_5_data_2.xlsx"
history_file = open("gpt_3.5_happiness_5_history_2.txt", "a")
all_answers_file = open('gpt_3.5_happiness_5_data_2.pickle', 'ab')
model_engine = "gpt-3.5-turbo-0301"
iterations = 980
count = 0
n=1

while count < iterations:
    try:
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=[{"role": "user", "content": question}],
            max_tokens=2048,
            #Number of attempts per randomized permutation
            n=n,
            stop=None,
            temperature=1.0
                    )
        answers_list = [answer for answer in response['choices'][0]['message']['content'].split('\n') if answer != ""]
        if len(answers_list) > 1:
            names_list = [None] * len(answers_list)
            names_list = create_names(master_name, answers_list)
        else:
            names_list = [master_name] 

        answer = Answer(iteration = count, master_name = master_name, names_list = names_list, full_answer = response['choices'][0]['message']['content'], answers_list = answers_list)
        pickle.dump(answer, all_answers_file)
        all_answers_file.flush()
                    
        df.loc[count, names_list] = answers_list
        df.to_excel(output_df, index=False)
        #if there is a duplicate axes error, it means that some of the names already exist in the df, and some don't
                    
        success_message = 'Iteration: '+str(count) + "\nMaster_name: " + str(master_name) + "\nSuccess" +"\n" #+ "\nNames_list: " + str(names_list) + "\nAnswers_list: " + str(answers_list) + "\n"
        print(success_message)
        history_file.write(success_message)
        history_file.flush()
        count +=1
    except Exception as e:
        error_message = 'Iteration: ' + str(count) + '\nMaster_name: ' + str(master_name) + "\nError,trying again in 60 seconds\n" + str(e) + "\n"
        print(error_message) 
        history_file.write(error_message)
        history_file.flush()
        time.sleep(60)

history_file.close
all_answers_file.close

df1 = pd.read_excel("gpt_3.5_happiness_5_data_1.xlsx")
df2 = pd.read_excel("gpt_3.5_happiness_5_data_2.xlsx")

df_concat = pd.concat([df1,df2]).astype(str)

df_final = df_concat.applymap(lambda x: x.strip(".0"))

df_final.to_excel('final_gpt_3.5_happiness_5_data.xlsx', index=False)
    
