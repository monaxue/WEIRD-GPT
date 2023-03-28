import openai
import os

# Use " setx OPENAI_API_KEY "your-api-key" " in the command prompt to set your API key as an evironmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

runs = 2

answers = []

for i in range(runs):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=[{"role": "user", "content": "People sometimes talk about what the aims of their country should be for the next ten years. I’ve listed some goals that different people would give different priorities. Which one of these would an average human consider the most important? Which one of these would the average person consider next most important? Please respond in a numbered list where your first item on the list is the number of the goal that is most important, and your second item on the list is the number of the goal that is next most important. Please respond only using a single number, with no words.\n1. A high level of economic growth\n2. Making sure this country has strong defense forces\n3. Seeing that people have more say about how things are done at their jobs and in their communities\n4. Trying to make our cities and countryside more beautiful"
}], temperature=1, max_tokens=100)
    answers.append(response['choices'][0]['message']['content']) 

print(answers)