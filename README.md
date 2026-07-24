# 🚀 LLM Application Practice Questions

Collection of Basic Python LLM applications built with the official **Google Gemini SDK** (`google-genai`) demonstrating practical LLM workflows: prompt engineering, system instructions, persona adoption, multi-language translation, tone modification, and automated question generation.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Applications Breakdown](#-applications-breakdown)
  - [1. Language Translator](#1-language-translator)
  - [2. Multi-Language Translator Assistant](#2-multi-language-translator-assistant)
  - [3. Multi-Type Question Generator Assistant](#3-multi-type-question-generator-assistant)
  - [4. Persona-Based Study Assistant](#4-persona-based-study-assistant)
  - [5. Persona-Based Tone Modifier Assistant](#5-persona-based-tone-modifier-assistant)
  - [6. Question Generator](#6-question-generator)
  - [7. Study Assistant](#7-study-assistant)
  - [8. Tone Modifier](#8-tone-modifier)
  - [9. Interactive Language Translator](#9-interactive-language-translator)
  - [10. Interactive Question Generator](#10-interactive-question-generator)
  - [11. Interactive Study Assistant](#11-interactive-study-assistant)
- [Tech Stack & Prerequisites](#-tech-stack--prerequisites)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [Directory Structure](#-directory-structure)
- [Security & Environment Variables](#-security--environment-variables)

---

## 🌟 Overview

This repository contains practice applications designed to learn different patterns when working with Large Language Models (LLMs) using Google's `gemini-2.5-flash` model:

- **Basic Prompting**: Direct task execution via user prompts.
- **System Instructions**: Configuring system-level behavior using `google.genai.types.GenerateContentConfig`.
- **Persona & Tone Switching**: Adjusting model responses according to user roles, tones, and target audiences.
- **Gradio UI**: Using Gradio to make the application interactive.
---

## 🛠 Applications Breakdown

### 1. Language Translator
- **Path**: `LanguageTranslator/app.py`
- **Description**: Translates input text into Hindi using basic prompt engineering.
- **Key Concepts**: Basic LLM API client call, direct prompt formatting.
- **Model**: `gemini-2.5-flash`

### 2. Multi-Language Translator Assistant
- **Path**: `Multi-Language Translator Assistant/app.py`
- **Description**: Translates text into target languages (Hindi, Telugu, French) using custom system instructions per language.
- **Key Concepts**: `GenerateContentConfig`, `system_instruction`, setting `temperature` (0.3) and `max_output_tokens`.
- **Model**: `gemini-2.5-flash`

### 3. Multi-Type Question Generator Assistant
- **Path**: `Multi-Type Question Generator Assistant/app.py`
- **Description**: Takes source content and automatically generates MCQs, Short Answer, or Interview questions.
- **Key Concepts**: Instructor persona system instructions, custom temperature tuning (0.4).
- **Model**: `gemini-2.5-flash`

### 4. Persona-Based Study Assistant
- **Path**: `Persona-Based Study Assistant/app.py`
- **Description**: Explains complex concepts by adopting different teaching personas (e.g., **Friendly** with beginner-friendly analogies vs. **Academic** with formal university professor style).
- **Key Concepts**: Persona prompting, dynamic system instructions.
- **Model**: `gemini-2.5-flash`

### 5. Persona-Based Tone Modifier Assistant
- **Path**: `Persona-Based Tone Modifier Assistant/app.py`
- **Description**: Re-writes input sentences into specific styles (**Formal** or **Casual**) using system-level instruction rules.
- **Key Concepts**: Tone control via system instructions, output token constraints.
- **Model**: `gemini-2.5-flash`

### 6. Question Generator
- **Path**: `Question Generator/app.py`
- **Description**: Generates practice and comprehension questions based on provided text passages.
- **Key Concepts**: Content summarization and test case generation via direct prompting.
- **Model**: `gemini-2.5-flash`

### 7. Study Assistant
- **Path**: `Study Assistant/app.py`
- **Description**: Interactive AI study companion designed for open-ended learning and concept breakdowns.
- **Key Concepts**: Reusable function wrapping for LLM queries.
- **Model**: `gemini-2.5-flash`

### 8. Tone Modifier
- **Path**: `Tone Modifier/app.py`
- **Description**: Transforms text tone (e.g., changing normal statements into an angry or formal tone).
- **Key Concepts**: Zero-shot tone modification.
- **Model**: `gemini-2.5-flash`

### 9. Interactive Language Translator
- **Path**: `Interactive Language Translator/app.py`
- **Description**: Translates input text into Hindi, Telugu, or French using custon system instructions and radio buttons for language selection.
- **Key Concepts**: UI implementation using Gradio to make the application interactive.
- **Model**: `gemini-2.5-flash`

### 10. Interactive Question Generator
- **Path**: `Interactive Question Generator/app.py`
- **Description**: Generates questions based on the input text using custom system instructions and radio buttons for question type selection.
- **Key Concepts**: UI implementation using Gradio to make the application interactive.
- **Model**: `gemini-2.5-flash`

### 11. Interactive Study Assistant
- **Path**: `Interactive Study Assistant/app.py`
- **Description**: Explains complex concepts by adopting different teaching personas (e.g., **Friendly** with beginner-friendly analogies vs. **Academic** with formal university professor style).
- **Key Concepts**: UI implementation using Gradio to make the application interactive.
- **Model**: `gemini-2.5-flash`
---
## 💻 Tech Stack & Prerequisites

- **Python**: 3.9 or higher
- **SDK**: `google-genai` (Official Google GenAI SDK)
- **Environment Management**: `python-dotenv`
- **UI**: `gradio`
- **LLM Engine**: Google Gemini API (`gemini-2.5-flash`)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SparshWasan/LLM-Applications.git
cd "LLM Applications"
```

### 2. Install Dependencies
```bash
pip install google-genai python-dotenv gradio 
```

### 3. Setup Environment Variables
1. Copy the sample environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and paste your Google Gemini API key (obtainable from [Google AI Studio](https://aistudio.google.com/)):
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

---

## Usage Guide

You can run any `app.py` script either by navigating into its folder or executing it directly from the workspace root directory:

### Option A: From folder
```bash
cd "Persona-Based Study Assistant"
python app.py
```

### Option B: From root
```bash
python "Multi-Language Translator Assistant/app.py"
```

> 💡 **Windows Terminal Tip**: When running scripts that return non-ASCII characters (such as Hindi or Telugu script), set UTF-8 encoding in PowerShell to prevent `UnicodeEncodeError`:
> ```powershell
> $env:PYTHONIOENCODING="utf-8"
> python "LanguageTranslator/app.py"
> ```

---

## 📂 Directory Structure

```text
LLM Applications/
├── .env                                         # Private API key (Ignored by Git)
├── .env.example                                 # Environment template for GitHub
├── .gitignore                                   # Prevents pushing sensitive files
├── README.md                                    # Repository documentation
│
├── LanguageTranslator/
│   └── app.py                                   # Basic Hindi translation
├── Multi-Language Translator Assistant/
│   └── app.py                                   # System-prompt driven multi-language translation
├── Multi-Type Question Generator Assistant/
│   └── app.py                                   # MCQs, Short Answer & Interview question generator
├── Persona-Based Study Assistant/
│   └── app.py                                   # Friendly vs Academic tutor personas
├── Persona-Based Tone Modifier Assistant/
│   └── app.py                                   # Formal vs Casual sentence rewriting
├── Question Generator/
│   └── app.py                                   # General question generator from text
├── Study Assistant/
│   └── app.py                                   # General AI study companion
├── Tone Modifier/
│    └── app.py                                   # Direct tone transformation
├── Interactive Language Translator/
│    └── app.py                                   # Interactive language translator
├── Interactive Question Generator/
│    └── app.py                                   # Interactive question generator
├── Interactive Study Assistant/
│    └── app.py                                   # Interactive study assistant
```
---