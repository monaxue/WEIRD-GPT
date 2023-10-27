import pandas as pd
import openai
import os
import time

rate_limit_per_minute = 3500.0
delay = 60.0 / rate_limit_per_minute

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

iterations = 2
df = pd.DataFrame()

prompts = pd.read_csv('V2/WVS/WVS_v2_all_languages.csv') 

count = 0
while count < iterations:
    j = 0
    while j < prompts.shape[0]:
        item = prompts.loc[j, "Prompt"]
        try:
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo-0301",
                temperature = 1.0,
                messages=[{"role": "user", "content": str(item)}]
            )
            answer = response['choices'][0]['message']['content']

            df.loc[count, prompts.loc[j, "Name"]] = answer
            df.to_csv("tests\\answers.csv", index=False)
            
            success_message = 'Iteration: '+str(count) + "\nPrompt name: " + str(prompts.loc[j, "Name"]) + "\nSuccess" +"\n"
            print(success_message)

            time.sleep(delay)
            j+=1
        except Exception as e:
            error_message = 'Iteration: ' + str(count) + '\nPrompt name: ' + str(prompts.loc[j, "Name"]) + "\nError, trying again in 60 seconds\n" + str(e) + "\n"
            print(error_message) 
            time.sleep(60)       
    count +=1

