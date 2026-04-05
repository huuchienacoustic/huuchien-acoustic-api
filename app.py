from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "OK",
        "message": "HuuChien Acoustic API running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })