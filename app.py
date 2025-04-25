
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCl1fPNdHYj47f7NgPwl9_ZoHWyae5v-S4"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("question", "")
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }
    response = requests.post(GEMINI_URL, headers=headers, json=data)
    if response.status_code == 200:
        gemini_reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"reply": gemini_reply})
    else:
        return jsonify({"reply": "Sorry, something went wrong."}), 500

if __name__ == "__main__":
    app.run(debug=True)
