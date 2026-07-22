from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def study_assistant(user_prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=user_prompt
    )
    return response

result = study_assistant("Explain Gen AI")
print(result.text)