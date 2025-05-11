from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess  # Add this at the top

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React app

# Dummy user data for testing
users = {
    "user@example.com": "password123"
}

@app.route('/launch-game', methods=['GET'])
def launch_game():
    try:
        # Replace 'python' with 'python3' if needed
        subprocess.Popen(['python', 'flappy2.py'])  # Your Flappy Bird file
        return jsonify({"message": "Game launched successfully!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if users.get(email) == password:
        # Successful login
        return jsonify({"message": "Login successful", "status": "success"}), 200
    else:
        # Failed login
        return jsonify({"message": "Invalid credentials", "status": "error"}), 401

if __name__ == '__main__':
    app.run(port=5000)
