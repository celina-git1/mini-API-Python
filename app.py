from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Découvrez notre mini API Flask"})

@app.route("/status", methods=["GET"])
def status():
    now = datetime.now().isoformat()
    return jsonify({"status": "API fonctionnelle", "timestamp": now})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Accès aux données depuis GCS à intégrer"})

@app.route("/data", methods=["POST"])
def post_data():
    return jsonify({"message": "Ajout des données dans GCS à implémenter"})

@app.route("/joke", methods=["GET"])
def get_joke():
    return jsonify({"joke": "Blague générée par Vertex AI"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

