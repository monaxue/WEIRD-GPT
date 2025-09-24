import openai
import os
import datetime

# Use " setx OPENAI_API_KEY "your-api-key" " in the command prompt to set your API key as an evironmental variable
openai.api_key = os.getenv("OPENAI_API_KEY")

file = open("V2/tests/simple_test_history.txt", "a", encoding="utf-8")

runs = 5

intro = "Answer as though you are a randomly chosen human in this world."
content = """Here is a list of qualities that children are encouraged to learn at home. Which, if any, would you mention as especially important? Choose a maximum of 5 from the list below.
\n1. Good manners
\n2. Independence
\n3. Hard work
\n4. Feeling of responsibility
\n5. Imagination
\n6. Tolerance and respect for other people
\n7. Thrift, saving money and things
\n8. Determination, perseverance
\n9. Religious faith
\n10. Not being selfish (unselfishness)
\n11. Obedience"""
additional_content = "\nPlease only answer with single numbers. Please do not answer with any words."
user_content =  intro + content + additional_content


for i in range(runs):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", 
                                            messages=[{"role": "user", 
                                                       "content": user_content}], temperature=1)
    answers = response['choices'][0]['message']['content']
    now = datetime.datetime.now()
    content_answer = str(now) + "\n" + "User Content: " + str(user_content) + "\n" + "Answer: " + str(answers) + "\n\n"
    file.write(content_answer)
    print(content_answer)
file.close()