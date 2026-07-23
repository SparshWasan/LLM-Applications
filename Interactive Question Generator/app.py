import os 
import gradio as gr
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

question_types = {
    "MCQs": "Generate multiple-choice questions along with their correct answers from the given content.",
    "Short Answer": "Generate short-answer questions along with their correct answers from the given content.",
    "Interview": "Generate interview-style questions along with their correct answers from the given content."
}

def question_generator(content, q_type):
    system_prompt = question_types[q_type]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=content
    )
    return response.text

demo = gr.Interface(
    fn=question_generator,
    inputs=[
        gr.Textbox(lines=6, placeholder="Enter or paste the content here...", label="Content Textbox"),
        gr.Radio(choices=list(question_types.keys()), value="MCQs", label="Question Type")
    ],
    outputs=gr.Textbox(lines=12, label="Generated Questions"),
    title="Interactive Question Generator",
    description="In this project, let's build an Interactive Question Generator Application using Google Gemini API along with Gradio to generate different types of questions from a given content through a simple web interface."
)

demo.launch(server_name="0.0.0.0", root_path="/gradio", share=True)