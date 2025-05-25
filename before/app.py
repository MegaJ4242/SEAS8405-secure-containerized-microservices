from flask import Flask, request, jsonify
import os
import subprocess
import ast
import re

app = Flask(__name__)

# Load password from environment variable
PASSWORD = os.environ.get("APP_PASSWORD", "default_dev_password")

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    if not name.isalnum():
        return jsonify({"error": "Invalid name"}), 400
    return f"Hello, {name}!"

@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    # Validate basic IPv4 format (e.g., 8.8.8.8)
    if not ip or not re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
        return jsonify({"error": "Invalid IP address"}), 400
    try:
        result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True, timeout=5)
        return f"<pre>{result.stdout}</pre>"
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Ping timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

import numexpr

@app.route('/calculate')
def calculate():
    expression = request.args.get('expr')
    try:
        # Evaluate safely using numexpr
        result = numexpr.evaluate(expression).item()
        return str(result)
    except Exception as e:
        return jsonify({"error": f"Invalid expression: {str(e)}"}), 400

# Run only on localhost
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

