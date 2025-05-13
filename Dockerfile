FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copie tous les fichiers du projet dans le conteneur
COPY . .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Variables d’environnement (à modifier si besoin)
ENV PROJECT_ID="mini-api-459410"
ENV REGION="europe-west1"
ENV BUCKET_NAME="bucket-mini-api"
ENV FILE_NAME="data.json"  # ❗ juste le chemin dans le bucket, pas besoin de répéter le nom du bucket

# Exposer le port Flask
EXPOSE 5000

# Commande de lancement
CMD ["python", "app.py"]
