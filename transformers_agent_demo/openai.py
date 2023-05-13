import os

from transformers import OpenAiAgent


def text_davinci_003():
    agent = OpenAiAgent(model="text-davinci-003", api_key=os.getenv("OPENAI_API_KEY"))
    agent.run("Draw me a picture of rivers and lakes.")
