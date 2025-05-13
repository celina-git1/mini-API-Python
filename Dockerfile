# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définir les variables d’environnement (changées via docker run si besoin)
ENV PROJECT_ID="mini-api-459410"
ENV REGION="europe-west1"
ENV BUCKET_NAME="bucket-mini-api"
ENV FILE_NAME="data.json"
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/gcp-key.json"

# Exposer le port de l'application Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
