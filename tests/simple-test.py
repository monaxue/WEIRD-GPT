import openai
import os

# Use " setx OPENAI_API_KEY "your-api-key" " in the command prompt to set your API key as an evironmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(model="text-davinci-003", prompt="List 10 objects.", temperature=0, max_tokens=100)

print(response)