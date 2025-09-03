from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    # Simple AI logic (baad me advanced connect karenge)
    if "hello" in user_input.lower():
        response = "Hi Shaurya! 👋 How are you?"
    elif "how are you" in user_input.lower():
        response = "I'm doing great, thanks for asking! 🚀"
    else:
        response = "Sorry, I didn’t understand. Can you rephrase?"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
