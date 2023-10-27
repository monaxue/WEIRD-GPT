import openai
import os
import datetime

# Use " setx OPENAI_API_KEY "your-api-key" " in the command prompt to set your API key as an evironmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

file = open("V2/tests/simple_test_history.txt", "a")

runs = 1

system_content = ""
system_user_content = "You are a randomly chosen human in this world. "
user_content = system_user_content + "For the following group of people, would you mention them as people you would not like to have as neighbors? Please answer with either 1 or 2, where 1 is 'would mention' and 2 is 'would not mention.' Please only answer using a single number, with no words. The group of people is: Drug addicts."


for i in range(runs):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", 
                                            messages=[{"role": "system", "content": system_content,
                                                "role": "user", 
                                                       "content": user_content
}], temperature=1, max_tokens=100)
    answers = response['choices'][0]['message']['content']

now = datetime.datetime.now()
content_answer = str(now) + "\n" + "System Content: " + str(system_content) +"\n" + "User Content: " + str(user_content) + "\n" + "Answer: " + str(answers) + "\n\n"
file.write(content_answer)
print(content_answer)

file.close()