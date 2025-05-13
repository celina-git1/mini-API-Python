from flask import Flask, jsonify, request
from datetime import datetime
import os
import csv
import json
from google.cloud import storage
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession

app = Flask(__name__)

# Initialisation Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("REGION"))
model = GenerativeModel("gemini-2.0-flash-001")
chat: ChatSession = model.start_chat()

# Variables d'environnement (doivent être définies avant exécution)
BUCKET_NAME = os.environ.get("BUCKET_NAME")
FILE_NAME = os.environ.get("FILE_NAME")

# Clients GCP
storage_client = storage.Client()

# GET /hello
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Découvrez notre mini API Flask"})

# GET /status
@app.route("/status", methods=["GET"])
def status():
    now = datetime.now().isoformat()
    return jsonify({"status": "API fonctionnelle", "timestamp": now})

# GET /data
@app.route("/data", methods=["GET"])
def get_data():
    try:
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        content = blob.download_as_text()
        
        if FILE_NAME.endswith(".json"):
            data = json.loads(content)
        elif FILE_NAME.endswith(".csv"):
            data = list(csv.DictReader(content.splitlines()))
        else:
            return jsonify({"error": "Format non supporté"}), 400

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST /data
@app.route("/data", methods=["POST"])
def post_data():
    try:
        new_entry = request.get_json()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(FILE_NAME)
        content = blob.download_as_text()

        if FILE_NAME.endswith(".json"):
            data = json.loads(content)
            data.append(new_entry)
            blob.upload_from_string(json.dumps(data, indent=2), content_type="application/json")
        elif FILE_NAME.endswith(".csv"):
            lines = content.splitlines()
            reader = csv.DictReader(lines)
            fieldnames = reader.fieldnames
            output = lines + [",".join([str(new_entry.get(f, "")) for f in fieldnames])]
            blob.upload_from_string("\n".join(output), content_type="text/csv")
        else:
            return jsonify({"error": "Format non supporté"}), 400

        return jsonify({"message": "Entrée ajoutée avec succès"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET /joke
@app.route("/joke", methods=["GET"])
def joke():
    try:
        prompt = "Raconte une blague drôle et courte en français."
        response = chat.send_message(prompt)
        return jsonify({"joke": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Lancement serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
