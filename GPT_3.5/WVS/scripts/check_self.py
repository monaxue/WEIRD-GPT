import pandas as pd
import csv

df = pd.read_csv('check_self.csv')

print(df.columns)

table = [df.self_1.tolist(), df.self_2.tolist(), df.self_3.tolist(), df.self_4.tolist(), df.self_5.tolist(), df.self_6.tolist(), df.self_7.tolist(), df.self_8.tolist(), df.self_9.tolist(), df.self_10.tolist()]

table_unique = set(value for row in table for value in row)

list = sorted(table_unique)

print(list)

with open('unique.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for item in list:
        writer.writerow([item])



