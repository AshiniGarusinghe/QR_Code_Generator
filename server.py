from flask import Flask, request, jsonify
from flask_cors import CORS
import qrcode
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

# Ensure 'static' folder exists to save QR codes
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json
    unique_data = f"{data['name']} - {data['email']}"

    qr = qrcode.make(unique_data)
    qr_path = f"static/{data['email']}.png"
    qr.save(qr_path)

    return jsonify({"qr_code": qr_path})

if __name__ == "__main__":
    app.run(debug=True)
