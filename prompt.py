import openai
import os

openai.api_key = os.getenv('API_KEY')
prompt = "ENTER TEXT HERE"
  
openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=1000,
  )
