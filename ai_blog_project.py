#ai blog project
#used a config file to store my api key

import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic, paragraph_number, short_summary):
    if short_summary == 'Y':
        prompt = f"Write {paragraph_number} paragraph and a short summary about {paragraph_topic}."
    else:
        prompt = f"Write {paragraph_number} paragraph about {paragraph_topic}."

    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=420,
        temperature=0.4
    )

    retrieve_blog = response.choices[0].text
    return retrieve_blog

keep_writing = True

while keep_writing == True: 
  print()
  answer = input("Write a paragraph? (Y/N): ").upper().strip()
  if answer == 'Y':
    user_topic = input ("What would you like me to write about?: ")
    paragraph_number = input ("How many paragraphs would you like? (1-3): ")
    
    short_summary = input ("Would you like a summary of the writeups? (Y/N): ").upper().strip()    
    print (generate_blog(user_topic,paragraph_number,short_summary))   

  else:
    keep_writing = False