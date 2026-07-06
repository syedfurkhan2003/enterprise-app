from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket
import datetime

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return jsonify({
        "application": "Enterprise GitOps Platform",
        "status": "Running",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "time": str(datetime.datetime.now())
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/version")
def version():
    return jsonify({
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)