from flask import Flask, jsonify, request
from datetime import datetime
from google.cloud import aiplatform
import os

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


import os
from vertexai.preview.generative_models import GenerativeModel, ChatSession
from flask import Flask
 
app = Flask(__name__)
 

vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("REGION"))
 

model = GenerativeModel(model_name="gemini-2.0-flash-001")
 

chat: ChatSession = model.start_chat()
 
@app.route("/joke")
def joke():
    
    prompt = "Raconte une blague drôle et courte."
 
    
    response = chat.send_message(prompt)
 
    
    return {"joke": response.text}
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

