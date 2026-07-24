from logging import debug
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import gradio as gr

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

languages = {
    "Hindi": "Translate the given sentence into Hindi.",
    "Telugu": "Translate the given sentence into Telugu.",
    "French": "Translate the given sentence into French."
}

def language_translator(question, language):
    system_prompt = languages[language]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=question
    )
    return response.text

demo = gr.Interface(
    fn=language_translator,
    inputs=[
        gr.Textbox(lines=4, placeholder="Enter text to translate here...",label="Input Sentence"),
        gr.Radio(choices=list(languages.keys()), value="Hindi", label="Target Language")
    ],
    outputs = gr.Textbox(lines=10, label="Translated Output"),
    title = "Interactive Language Translator",
    description="Translates the given text into specified language."
)

demo.launch(server_name="0.0.0.0", root_path="/gradio", share=True)