import pickle

class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answers_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answers_list = answers_list

data1 = []
with open('gpt_3.5_wvs_data_1.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            data1.append(obj)
        except EOFError:
            # End of file reached
            break


data2 = []
with open('gpt_3.5_wvs_data_2.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data1[len(data1)-1].iteration
            data2.append(obj)
        except EOFError:
            # End of file reached
            break

combined_data = []

for obj in data1 + data2:
    combined_data.append(obj)


with open('final_gpt_3.5_wvs_data.pickle', 'wb') as file:
    pickle.dump(combined_data, file)
