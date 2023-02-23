import pandas as pd

#list of survey questions in original order
survey1_names = ["A_1", "A_2"]
survey2_names = ["B_1", "B_2"]
survey3_names = ["C"]
survey_items_names = [survey1_names, survey2_names, survey3_names]

survey1_subitems = ["1+1=?", "1+2=?"]
survey2_subitems = ["list two numbers with decimals", "list two fractions"]
survey3_subitems = ["List 2 objects."]
survey_items = [survey1_subitems, survey2_subitems, survey3_subitems]

number_of_items = len(survey_items)

df = pd.DataFrame(columns=['A_1', 'A_2', 'B_1_1', 'B_1_2', 'B_2_1', 'B_2_2', 'C_1', 'C_2'])