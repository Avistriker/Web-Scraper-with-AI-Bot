# Web Scraper with AI Bot (Web Striker 4.0)

## Overview
Web Striker 4.0 is a web scraper integrated with an AI chatbot. It allows users to scrape text content from a website, summarize it using AI, and interact with an AI chatbot for contextual discussions. This project utilizes Flask for the backend, BeautifulSoup for web scraping, and Groq Cloud's LLMs for text processing. The chatbot supports model selection between `Gemma2 💎` and `Mixtral 🚀`.

## Features
- Scrape text content from any public website.
- Summarize the scraped content using AI.
- Interact with an AI chatbot based on scraped and summarized content.
- Choose between different AI models for processing.
- Simple and user-friendly web interface.

## Technologies Used
- **Python** (Flask, Requests, BeautifulSoup)
- **JavaScript** (Frontend UI & interactions)
- **HTML/CSS** (User interface)
- **Groq Cloud** (AI-powered summarization & chatbot)
- **Ollama** (For local AI processing, if needed)

## Installation & Setup
### Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)
- BeautifulSoup (`pip install beautifulsoup4`)
- Groq SDK (`pip install groq`)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/web-striker-4.0.git
   cd web-striker-4.0
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up API keys (Modify `GROQ_API_KEY` in `app.py` and `scraper.py`).
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open `http://127.0.0.1:5000/` in your browser.

## API Endpoints
### 1. Home Page
- **Route:** `/`
- **Method:** `GET`
- **Description:** Serves the frontend UI.

### 2. Web Scraping & Summarization
- **Route:** `/scrape`
- **Method:** `POST`
- **Request Body:** `{ "url": "<website_url>" }`
- **Response:** `{ "scraped_text": "...", "summary": "..." }`

### 3. Chatbot Interaction
- **Route:** `/chat`
- **Method:** `POST`
- **Request Body:** `{ "message": "<user_query>", "context": "<optional_context>" }`
- **Response:** `{ "response": "AI-generated response" }`

### 4. Model Selection
- **Route:** `/select_model`
- **Method:** `POST`
- **Request Body:** `{ "model": "Mixtral 🚀" }`
- **Response:** `{ "message": "Model changed to Mixtral 🚀" }`

## Frontend Features
- **Model selection dropdown** (Switch between Gemma2 💎 and Mixtral 🚀)
- **Scrape & Summarize Section** (Enter URL to scrape and summarize content)
- **Chatbot Section** (Engage in AI-powered discussions)

## Future Enhancements
- Implement Ollama for local AI processing.
- Add database support for storing scraped data.
- Enhance chatbot memory for better contextual understanding.

## License
This project is open-source and available under the MIT License.

---
**Author:** Avinash Kumar  
**Contact:** [avinashbksc007@gmail.com]  
**GitHub:** [https://github.com/Avistriker]

