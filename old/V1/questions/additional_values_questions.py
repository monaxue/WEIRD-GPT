# This is different than cognitive_questions.py becauase this uses the origianl inclusion tasks, instead of the ones we created.

import pandas as pd

# task 1
survey1_names = ['tightness-looseness_revised_1', 'tightness-looseness_revised_2', 'tightness-looseness_revised_3', 'tightness-looseness_revised_4', 'tightness-looseness_revised_5', 'tightness-looseness_revised_6']
survey1_items = [
    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nThere are many social norms that people are supposed to abide by in this country.",

    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nIn this country, there are very clear expectations for how people should act in most situations.",

    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nPeople agree upon what behaviors are appropriate versus inappropriate in most situations in this country.",

    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nPeople in this country have a great deal of freedom in deciding how they want to behave in most situations.",

    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nIn this country, if someone acts in an inappropriate way, others will strongly disapprove.",

    "For the statement below, please indicate how an average human would respond to the following questions. Note that the statements sometimes refer to ‘social norms,’ which are standards for behavior that are generally unwritten. Respond on a scale from 1 to 6 where 1 is ‘strongly disagree’, 2 is ‘moderately disagree’, 3 is ‘slightly disagree’, 4 is ‘slightly agree’, 5 is ‘moderately agree’, and 6 is ‘strongly agree’. Please only answer with a single number, with no words.\nPeople in this country almost always comply with social norms."

    ]

# task 2
survey2_names = ["honor_1", "honor_2", "honor_3", "honor_4", "honor_5", "honor_6", "honor_7", "honor_8"]
survey2_items = [
    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA man should love his family.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA man should feel committed toward his family.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA man should be vigilant about his romantic partner's social behavior.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA man should be vigilant about his romantic partner's interactions with other men.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nEveryone should love their own country.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nPeople should do their best to make their country proud.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA man should be responsive to his family's needs.",

    "For the statement below, please indicate how an average human would respond to the following questions. Respond on a scale from 1 to 7 where 1 is “strongly disagree”, 2 is “disagree”, 3 is “somewhat disagree”, 4 is “Neither agree nor disagree”, 5 is “somewhat agree”, 6 is “agree” and 7 is “strongly agree”. Please only answer with a single number, with no words.\nA real man always wants to make his romantic partner happy."
   ]

# task 3
survey3_names = ['h_individualism-collectivism_1', 'h_individualism-collectivism_2', 'h_individualism-collectivism_3', 'h_individualism-collectivism_4']
survey3_items = [
    "In choosing an ideal job, how important would it be to an average human to have sufficient time for their personal or home life? Please respond on a scale from 1 to 5 where 1 = “of utmost importance”, 2 = “very important”, 3 = “of moderate importance”, 4 = “of little importance”, and 5 = “of very little or no importance”. Please only answer with a single number, with no words.",

    "In choosing an ideal job, how important would it be to an average human to have security of employment? Please respond on a scale from 1 to 5 where 1 = “of utmost importance”, 2 = “very important”, 3 = “of moderate importance”, 4 = “of little importance”, and 5 = “of very little or no importance”. Please only answer with a single number, with no words.",

    "In choosing an ideal job, how important would it be to an average human to do work that is interesting? Please respond on a scale from 1 to 5 where 1 = “of utmost importance”, 2 = “very important”, 3 = “of moderate importance”, 4 = “of little importance”, and 5 = “of very little or no importance”. Please only answer with a single number, with no words.",
    
    "In choosing an ideal job, how important would it be to an average human to have a job respected by their family and friends? Please respond on a scale from 1 to 5 where 1 = “of utmost importance”, 2 = “very important”, 3 = “of moderate importance”, 4 = “of little importance”, and 5 = “of very little or no importance”. Please only answer with a single number, with no words."

]

# task 4


# task 5
survey_items_names = [survey1_names, survey2_names, survey3_names]
survey_items = [survey1_items, survey2_items, survey3_items]

number_of_items = len(survey_items)

df_i = pd.DataFrame(columns= [
    'tightness-looseness_revised_1', 'tightness-looseness_revised_2', 'tightness-looseness_revised_3', 'tightness-looseness_revised_4', 'tightness-looseness_revised_5', 'tightness-looseness_revised_6',

    "honor_1", "honor_2", "honor_3", "honor_4", "honor_5", "honor_6", "honor_7", "honor_8",

    'h_individualism-collectivism_1', 'h_individualism-collectivism_2', 'h_individualism-collectivism_3', 'h_individualism-collectivism_4'])