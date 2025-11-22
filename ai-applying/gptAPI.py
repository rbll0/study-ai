from email import message
from openai import OpenAI
import os

client = OpenAI()

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Escreva um hello world em python"
)

print(response.output_text)
