import pickle

data = []

class Answer:
    def __init__(self,iteration,master_name,names_list,full_answer,answer_list):
        self.iteration = iteration
        self.master_name = master_name
        self.names_list = names_list
        self.full_answer = full_answer
        self.answer_list = answer_list

with open('all_answers_cognitive_3.5_test.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            data.append(obj)
        except EOFError:
            # End of file reached
            break

for obj in data:
    for key, value in vars(obj).items():
        print(key, "=", value)

filtered_list = [obj for obj in data if (obj.iteration == 2) & (obj.master_name == 'triad')]

for obj in filtered_list:
    for key, value in vars(obj).items():
        print(key, "=", value)