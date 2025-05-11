from flask import Flask, jsonify
from datetime import datetime
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession 
import os
 
app = Flask(__name__)
 
# Route hello
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Découvrez notre mini API Flask"})
 
# Route status
@app.route("/status", methods=["GET"])
def status():
    now = datetime.now().isoformat()
    return jsonify({"status": "API fonctionnelle", "timestamp": now})
 
# Route data GET
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Accès aux données depuis GCS à intégrer"})
 
# Route data POST
@app.route("/data", methods=["POST"])
def post_data():
    return jsonify({"message": "Ajout des données dans GCS à implémenter"})
 
# Initialisation de VertexAI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("REGION"))
 
# Initialisation du modèle
model = GenerativeModel(model_name="gemini-2.0-flash-001")
chat: ChatSession = model.start_chat()
 
# Route joke
@app.route("/joke")
def joke():
    prompt = "Raconte une blague drôle et courte."
    response = chat.send_message(prompt)
    return {"joke": response.text}
 
# Lancement du serveur Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)