from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def language_translator(user_prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=user_prompt
    )
    return response

user_prompt = "I am Sparsh. I am a software developer. Translate the sentence in Hindi"
print(language_translator(user_prompt).text)