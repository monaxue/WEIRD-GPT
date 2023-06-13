import openai
import os

# Use " setx OPENAI_API_KEY "your-api-key" " in the command prompt to set your API key as an evironmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

runs = 2

answers = []

for i in range(runs):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=[{"role": "user", "content": "On this list are various types of people. What, if any, would the average human list as people they would like to have as neighbors? Please answer using a numbered list, and for each item, please answer with either 1 or 2, where 1 is “Yes” and 2 is “No”. Please answer only using a single number, with no words.\n1. Drug addicts\n2. People of a different race\n3. People who have AIDS\n4. Immigrants/foreign workers\n5. Homosexuals\n6. People of a different religion\n7. Heavy drinkers\n8. Unmarried couples living together\n9. People who speak a different language\nBy numbered list, I mean that each line should first have the line number, followed by a period, followed by a space, then followed by the answer. For instance, if the first answer is A, the second answer is B, and the third answer is C, your answer should look like: \n1. A\n2. B\n3. C"
}], temperature=1, max_tokens=100)
    answers.append(response['choices'][0]['message']['content']) 

print(answers)