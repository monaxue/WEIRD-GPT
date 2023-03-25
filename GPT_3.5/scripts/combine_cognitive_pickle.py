import pickle
import cognitive_questions_2
df = cognitive_questions_2.df_i.copy()


data3 = []
with open('all_answers_cognitive_3.5_new_3.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            data3.append(obj)
        except EOFError:
            # End of file reached
            break


data4 = []
with open('all_answers_cognitive_3.5_new_4.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data3[len(data3)-1].iteration
            data4.append(obj)
        except EOFError:
            # End of file reached
            break


data5 = []
with open('all_answers_cognitive_3.5_new_5.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data4[len(data4)-1].iteration
            data5.append(obj)
        except EOFError:
            # End of file reached
            break


data6 = []
with open('all_answers_cognitive_3.5_new_6.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data5[len(data5)-1].iteration
            data6.append(obj)
        except EOFError:
            # End of file reached
            break

data6_filtered = [obj for obj in data6 if (obj.iteration != data6[len(data6)-1].iteration)]

data7 = []
with open('all_answers_cognitive_3.5_new_7.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data6_filtered[len(data6_filtered)-1].iteration
            data7.append(obj)
        except EOFError:
            # End of file reached
            break

data8 = []
with open('all_answers_cognitive_3.5_new_8.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data7[len(data7)-1].iteration
            data8.append(obj)
        except EOFError:
            # End of file reached
            break

data8_filtered = [obj for obj in data8 if (obj.iteration != data8[len(data8)-1].iteration)]

data9 = []
with open('all_answers_cognitive_3.5_new_9.pickle', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            # Do something with the object here
            obj.iteration = obj.iteration + 1 + data8_filtered[len(data8_filtered)-1].iteration
            data9.append(obj)
        except EOFError:
            # End of file reached
            break


combined_data = []

for obj in data3 + data4 + data5 + data6_filtered + data7 + data8_filtered + data9:
    combined_data.append(obj)


with open('final_cognitive_3.5_new.pickle', 'wb') as file:
    pickle.dump(combined_data, file)
