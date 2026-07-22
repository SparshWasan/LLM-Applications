from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

languages = {
    "Hindi": "You are a professional translator. Translate the given text accurately into Hindi.",
    "Telugu": "You are a professional translator. Translate the given text accurately into Telugu.",
    "French": "You are a professional translator. Translate the given text accurately into French."
}

def language_translator(question, language):
    selected_language = languages[language]
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=selected_language,
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=question
    )
    return response.text

user_prompt = "I am Sparsh. I am a software developer"
language = "French"
result = language_translator(user_prompt, language)
print(result)