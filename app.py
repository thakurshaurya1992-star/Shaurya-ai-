from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Yahan apna OpenAI API key daalna
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",   # Free ke liye GPT-3.5 use karo
        messages=[{"role": "user", "content": user_input}]
    )

    bot_reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
