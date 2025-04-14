from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from rag import rag_chain as create_rag_chain

load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers="*")

# Home page route for the UI
@app.route('/')
def home():
    return render_template('index.html')

# Route to return hotel analytics
@app.route('/analytics', methods=['GET'])
def visualize():
    file_path = './data/hotel_analytics.json'
    if not os.path.exists(file_path):
        return jsonify({"error": "Run analytics.py to generate the .json file"}), 404
    with open(file_path, 'r') as f:
        analytics_data = json.load(f)
    return jsonify(analytics_data)

# Route to answer questions using RAG
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    api_key = request.headers.get("Authorization")
    if not api_key:
        return jsonify({"error": "No API key provided in the Authorization header"}), 401

    # Initialize the RAG chain instance
    rag_chain_instance = create_rag_chain()

    try:
        answer = rag_chain_instance.invoke(question)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": f"Error while processing the question: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
