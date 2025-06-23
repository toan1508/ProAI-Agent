from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "AIzaSyCVa1JCtWY2jtaUIRuS9D4tvlb9K-nHC-s"

@app.route("/")
def home():
    return "✅ Welcome to AI Pro Agent!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")

    try:
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}",
            headers={"Content-Type": "application/json"},
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ]
            }
        )
        result = response.json()
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"reply": reply})
    except Exception as e:
        print("❌ Lỗi khi gọi Gemini:", e)
        return jsonify({"reply": "❌ Đã có lỗi khi gọi Gemini API."})
