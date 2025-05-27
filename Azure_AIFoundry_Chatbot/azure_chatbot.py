import os
from aifoundry.core import AIFoundry

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
key = os.getenv("AZURE_OPENAI_KEY")

ai_foundry = AIFoundry(endpoint=endpoint, api_key=key)

def chat(user_input):
    response = ai_foundry.chat(model="gpt-4", messages=[{"role": "user", "content": user_input}])
    return response["choices"][0]["message"]["content"]

print("Azure AI Foundry chatbot ready.")
