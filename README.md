# AI Study Assistant 📚

A beginner-friendly, open-source study helper built with Python and Streamlit.

## Features

- **Summarize notes:** selects high-scoring sentences from pasted text.
- **Extract key terms:** finds frequently occurring words.
- **Revision prompts:** creates simple flashcard prompts from key terms.
- **No API key required:** runs locally and does not send your notes to an external AI service.

> **Important:** The first version uses lightweight, rule-based text processing. It is not a true generative-AI system, and its output may miss context or produce imperfect summaries. Always verify results against your original material.

## Demo

Run the app locally and paste a few paragraphs of lecture notes into any tab.

## Requirements

- Python 3.9 or newer
- pip

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-study-assistant.git
   cd ai-study-assistant
   ```

2. (Recommended) Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

Streamlit will open the app in your browser. If it does not, open the local URL shown in the terminal (usually `http://localhost:8501`).

## Privacy

This starter app processes pasted text in the running Python application. It has no database, analytics, or external AI API integration. If you deploy it publicly, review the hosting provider's privacy practices.

## Roadmap

- Add optional LLM-powered explanations with a clearly documented API setup.
- Generate multiple-choice questions with answer explanations.
- Support uploading TXT and PDF study notes.
- Add tests for text-processing functions.
- Improve multilingual stop-word handling.

## Contributing

Issues and pull requests are welcome. Please describe the change and include steps to reproduce bugs.

## Project status

Early prototype. It has not yet established users, downloads, or community adoption. Contributions and feedback are welcome.
