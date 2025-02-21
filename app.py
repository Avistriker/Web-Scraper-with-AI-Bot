from flask import Flask, request, jsonify, render_template
from scraper import scrape_website, summarize_text, chat_with_llm, select_model

app = Flask(__name__)

# Hardcoded API key (for testing only)
GROQ_API_KEY = "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"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_and_summarize():
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    # Scrape the website
    scraped_text = scrape_website(url)

    # Summarize the scraped text
    summary = summarize_text(scraped_text)

    return jsonify({
        "scraped_text": scraped_text,
        "summary": summary
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    context = data.get('context', '')

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    # Generate a response using the selected model
    response = chat_with_llm(user_message, context)

    return jsonify({
        "response": response
    })

@app.route('/select_model', methods=['POST'])
def change_model():
    data = request.json
    model_name = data.get('model')

    if not model_name:
        return jsonify({"error": "Model name is required"}), 400

    # Change the selected model
    result = select_model(model_name)

    return jsonify({
        "message": result
    })

if __name__ == '__main__':
    app.run(debug=True)