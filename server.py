import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server running!"

@app.route("/login", methods=["POST", "OPTIONS"])
def login():

    # Handle browser preflight
    if request.method == "OPTIONS":
        return "", 200

    data = request.get_json(force=True)

    user_id = data.get("id")
    name = data.get("name")

    with open("logins.txt", "a") as f:
        f.write(f"{datetime.now()} - {user_id} - {name}\n")

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

