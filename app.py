from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "OK", "message": "HuuChien Acoustic API running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# ==============================
# ROUTE TEST API
# ==============================
@app.route("/api/test", methods=["GET"])
def test_api():
    return jsonify({
        "result": "API working",
        "version": "1.0"
    })


# ==============================
# ROUTE UPLOAD FILE (chuẩn bị cho SaaS)
# ==============================
@app.route("/api/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    # demo xử lý (sau này bạn sẽ phân tích âm học ở đây)
    return jsonify({
        "filename": file.filename,
        "status": "uploaded successfully"
    })


# ==============================
# START SERVER (QUAN TRỌNG)
# ==============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)