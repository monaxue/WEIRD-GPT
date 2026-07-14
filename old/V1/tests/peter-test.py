import openai
import time
import numpy as np
import os

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

#Number of survey questions
number_of_questions=2

#Number of runs per randomized permutation
n=1

#list of survey questions in original order
survey_questions=["What is your name?\n", "A country is a nation.\nWhat country do you live in?\n"] 
model_engine = "text-davinci-003"
iterations = 1

count=0
file = open("filename.txt", "a")

while count < iterations:
    
    try:
        perm=np.random.permutation(number_of_questions)
        survey=""
        for i in range(number_of_questions):
            survey=survey+survey_questions[perm[i]]+"Question "+ str(i+1) +" (Multiple choice):\n"+"[blank]\n\n"

        response = openai.Completion.create(
            model=model_engine,
            prompt="Your task is to answer a survey of " + str(number_of_questions) + " questions. Given the incomplete survey, return each of the " + str(number_of_questions) + " questions, where every instance of [blank] is replaced with your answer. For each question, the [blank] should be replaced with only a single capitalized alphabet letter, and nothing more. For example, if you choose choice A, you should replace '[blank]' with 'A' and end the line immediately afterwards.\n\nIn summary, for each question, answer with only a single capital letter. Fill in the blanks step by step and only then return the completed survey.\n\n\nSURVEY:\n"+survey+"\n\n\nCHECKLIST FOR SURVEY ANSWERS:\nDid you answer all "+  str(number_of_questions)+" questions, from Question 1 to Question " +str(number_of_questions)+"?\nDid you do so only by replacing [blank] with your response?\nIs each of your answers exactly one capitalized letter long with no further explanations or symbols?\n\n\nSURVEY ANSWERS:\nQuestion 1 (Multiple choice):\n",
            max_tokens=2048,
            #Number of attempts per randomized permutation
            n=n,
            stop=None,
            temperature=1.0
        )
        answers = []
        for choice in response.choices:
            answers.append(choice.text)
        for answer in answers:
            file.write(str(perm)+"\nQuestion 1 (free response):\n" + answer + "\n\n")
        count +=1
        time.sleep(6*n)

    except:
        print("Error, trying again in 60 seconds")
        time.sleep(6*n)

    

file.close()













