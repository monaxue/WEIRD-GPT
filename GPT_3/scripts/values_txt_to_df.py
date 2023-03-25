import pandas as pd
import values_questions
import ast

df = values_questions.df_i.copy()

input_file = open("data/values/converted_values_history_1.txt", "r")

run = -1
# Loop over input string and extract lines between 'Iteration' and '['
for line in input_file:
    #print(line.split())
    if line.startswith('Iteration'):
        # Start of new iteration
        iteration_lines = []
        run0 = run
        run = int(line.split()[1])
        if run != run0:
            print("Iteration " +str(run))
    elif line.startswith('['):
        # End of iteration
        names = ast.literal_eval(line)
        if len(names) != len(iteration_lines):
            print("Mismatch between number of values and column names")
        if len(names) > len (iteration_lines):
            length = min(len(names), len(iteration_lines))
            names = names[:length]
            iteration_lines = iteration_lines[:length]
            # Add the values to the dataframe
            for c in range(length):
                df.loc[run, names[c]] = iteration_lines[c]
        if len(names) < len(iteration_lines):
            length = max(len(names), len(iteration_lines))
            names += [None] * (length - len(names))
            # Add the values to the dataframe
            for c in range(length):
                df.loc[run, names[c]] = iteration_lines[c]
        if len(names) == len(iteration_lines):
            for c in range(len(names)):
                df.loc[run, names[c]] = iteration_lines[c]
    else:
        # Inside iteration, add line to list
        answer = line.split()[0].strip(" .:-")
        iteration_lines.append(answer)
        #print("Answer "+str(answer))
    
        

    df.to_excel('cleaned_values_qs_1.xlsx', index=False)