One-Page Website Generator (Flask + OpenRouter)

Overview

This project is a simple AI-powered one-page website generator built with Python (Flask) and LLM APIs via OpenRouter.
A user provides a prompt describing the website they want, and the system generates a complete single-page HTML website with embedded CSS and JavaScript.

Built with:
- Flask (Backend API)
- OpenRouter (LLM + Embeddings)
- Stepfun step-3.5-flash
- Prompt engineering
- Limit usage to reduce token expenditure and prevent abuse


Features
- Generate full single-page websites from text prompts
- Supports HTML, CSS, and JavaScript in one file
- Uses OpenRouter API to access multiple LLM providers
- Flask API endpoint for frontend integration

Tech Stack

- Python
- Flask
- OpenAI Python SDK
- OpenRouter API
- LLM models

How It Works

1. A user sends a prompt describing the website they want.
2. The backend constructs a message list with:
    a system prompt (instructions for generating a webpage)
    the user prompt
3. The request is sent to an LLM via OpenRouter.
4. The model generates HTML code.
5. The completed HTML page is returned to the client.


How To Run Locally

1. Install Dependencies
pip install -r requirement.txt

2. Run Flask App
   -app.py

3. Test App:
   Api runs on http://127.0.0.1:5000
   Run test.py

License
This project is for educational and research purposes.

Author
Awwal Ajao