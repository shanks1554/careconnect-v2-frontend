from flask import Flask, render_template, request, redirect, session
import requests

app = Flask(__name__)
app.secret_key = "careconnect_secret"

BASE_URL = "https://care-connect-zg7l.onrender.com"
WAKE_URL = f"{BASE_URL}/wake"
CHAT_URL = f"{BASE_URL}/chat"
GREET_URL = f"{BASE_URL}/greet"

@app.route("/")
def wake():
    try:
        res = requests.get(WAKE_URL, timeout=10)
        if res.status_code == 200:
            return redirect("/chat")
    except Exception:
        pass
    return render_template("loader.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "messages" not in session:
        try:
            greet = requests.get(GREET_URL).json()
            session["messages"] = [{"sender": "bot", "text": greet["message"]}]
        except Exception:
            session["messages"] = [{"sender": "bot", "text": "Hello! (Greeting failed)"}]

    if request.method == "POST":
        user_msg = request.form["message"]
        session["messages"].append({"sender": "user", "text": user_msg})

        try:
            res = requests.post(CHAT_URL, json={"message": user_msg}, timeout=20)
            bot_msg = res.json().get("final", "Sorry, something went wrong.")
        except Exception:
            bot_msg = "Sorry, I couldn't reach the server."

        session["messages"].append({"sender": "bot", "text": bot_msg})
        session.modified = True
        return redirect("/chat")  # 🔥 FIX: prevent form resubmission

    return render_template("chat.html", messages=session["messages"])

@app.route("/clear")
def clear_chat():
    session.clear()
    return redirect("/chat")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)