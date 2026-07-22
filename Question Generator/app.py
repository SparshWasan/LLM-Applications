from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))

def question_generator(user_prompt):
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents=user_prompt
    )
    return response
text = "LLMs have limitations such as hallucination, knowledge cutoff and passiveness"
prompt = f"Generate questions from the following content: {text}"
result = question_generator(prompt)
print(result.text)