import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

question_types = {
    "MCQs": "Act as an experienced instructor. Create MCQ questions from the following content: ",
    "Short Answer": "Act as an experienced instructor. Create Short Answer questions from the following content: ",
    "Interview": "Act as an experienced instructor. Create Interview questions from the following content: "
}

def question_generator(content, q_type):
    selected_q_type = question_types[q_type]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=selected_q_type,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=content
    )
    return response.text

content = "LLMs have limitations such as hallucination, knowledge cutoff and passiveness"
q_type = "MCQs"
result = question_generator(content, q_type)
print(result)