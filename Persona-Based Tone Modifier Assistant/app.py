import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

tones = {
    "Formal" : "Change the tone to Formal of the following content.",
    "Casual" : "Change the tone to Casual of the following content.",
}

def study_assistant(sentence, tone):
    system_prompt = tones[tone]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000,
        ),
        contents=sentence
    )
    return response.text

sentence = "Kids are laughing outside the house"
tone = "Formal"
result = study_assistant(sentence, tone)

print(result)