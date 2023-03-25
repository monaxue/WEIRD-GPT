import pickle
import additional_values_questions
df = additional_values_questions.df_i.copy()

## Define functions and classes

def sub_numb(answer):
    period_ind = answer[:5].find('.')
    colon_ind = answer[:5].find(':')
    dash_ind = answer[:5].find('-')
    first_ind = min((ind for ind in [period_ind, colon_ind, dash_ind] if ind != -1), default=-1)
    
    if first_ind == -1:  # period, colon, and dash not found in the first 5 characters
        return 'na'
    else:
        return answer[:first_ind].strip()
    
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

class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answers_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answers_list = answers_list

## Import data from pickle file when there are multiple items in pickle file.

data = []
with open('gpt_3.5_additional_values_data_1.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            data.append(obj)
        except EOFError:
            # End of file reached
            break

## Import from pick file when there is only one item (can be a list of items) in pickle file

#with open('gpt_3.5_additional_values_data_1.pickle', 'rb') as file:
#    data = pickle.load(file)


## Other code:

#for obj in data:
#    for key, value in vars(obj).items():
#        print(key, "=", value)

filtered_list = [obj for obj in data if (obj.iteration == 9) & (obj.master_name == 'tightness-looseness_revised_6')]
print(filtered_list[0].full_answer)

for obj in filtered_list:
    for key, value in vars(obj).items():
        print(key, "=", value)




#for obj in data:
#    names_list_1 = [str(obj.master_name) + "_" + str(sub_numb(answer)) for answer in obj.answers_list]
#    df.loc[obj.iteration, names_list_1] = obj.answers_list
#
#df.to_excel('gpt_3.5_cognitive_test_1.xlsx', index=False)

#for obj in data:
#    df.loc[obj.iteration, obj.names_list] = [remove_extra(answer) for answer in obj.answers_list]
#
#df.to_excel('gpt_3.5_values_test_1.xlsx', index=False)