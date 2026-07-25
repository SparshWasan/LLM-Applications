import os
import gradio as gr
from google import genai 
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

tones = {
    "Formal": (
        "You are a tone translator that rewrites text into a formal, professional register. "
        "Produce a concise formal version preserving meaning, proper grammar, and polite phrasing."
    ),
    "Casual": (
        "You are a tone translator that rewrites text into a casual, friendly register. "
        "Use conversational phrasing, contractions, and a relaxed tone while preserving meaning."
    )
}

def tone_translator(sentence, persona):
   
    system_prompt = tones.get(persona, tones[persona])

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.3,
            max_output_tokens=2000
        ),
        contents=sentence
    )
    return response.text


demo = gr.Interface(
    fn = tone_translator,
    inputs=[
        gr.Textbox(lines=3, placeholder="Enter sentence to rewrite", label="Input Sentence"),
        gr.Radio(choices=list(tones.keys()), value="Formal", label="Tone Selector")
    ],
    outputs=gr.Textbox(lines=5, label="Rewritten Text"),
    title="Interactive Tone Translator",
    description="An LLM Application that changes the tone of the provided text into either formal or casual as per the users selection"
)

# demo.launch(server_name="0.0.0.0", root_path="/gradio", share=True)
demo.launch(debug=True)