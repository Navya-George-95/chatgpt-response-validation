import logging

import openai

from src.constants.constants import MODEL

class ChatGptAPI:
    @staticmethod
    def ask_chatgpt(question, model=MODEL, max_tokens=100, temperature=0):
    #Function to make an API request to GPT

        response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        max_tokens=max_tokens,
        temperature=temperature
        )

        logging.info(model)
        return response.choices[0].message['content'].strip()
