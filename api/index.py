from flask import Flask, request, jsonify
from custom_email import send_email
from utils.jokes import jokes
import random

app = Flask(__name__)

@app.route('/')
def index():
    return (
        "Welcome to the Joke API! Use the '/send-joke' endpoint to email a joke.<br><br>"
        "Here's an example of the joke payload you can use:<br>"
        "<pre>{\n"
        '    "name": "Ojas Mittal",\n'
        '    "email": "ojasmittal3108@gmail.com",\n'
        '    "joke": "Hello, this is a joke" => (This parameter is optional)\n'
        "}</pre>"
    )
@app.route('/send-joke', methods=['POST'])
def send_joke():
    data = request.json

    if not data:
        return jsonify({"error": "No data received"}), 400
    
    if not (data.get("name") or data.get("email")):
        return jsonify({"error": "Missing required fields name / email"}), 400

    name = data.get("name")
    email = data.get("email")
    joke = data.get("joke") or random.choice(jokes)

    try:
        send_email(name, email, joke)
    except Exception as e:
        return jsonify({"error": f"Failed to send email due to server error: {e}"}), 500
    
    return jsonify({"message": f"Email sent to {name} successfully!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)