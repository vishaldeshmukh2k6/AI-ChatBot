from flask import Flask, render_template, request, session, redirect, url_for
from responses import get_response
import requests

app = Flask(__name__)
app.secret_key = "chatbot_secret"

# Chatbot route
@app.route("/", methods=["GET", "POST"])
def chatbot():
    if "chat_history" not in session:
        session["chat_history"] = []
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)
        session["chat_history"].append({"user": user_input, "bot": bot_response})
    return render_template("chatbot.html", chat=session["chat_history"])

# Reset chat
@app.route("/reset")
def reset_chat():
    session["chat_history"] = []
    return redirect(url_for("chatbot"))  # Redirect to chatbot page


if __name__ == "__main__":
    app.run(debug=True, port=5001)
