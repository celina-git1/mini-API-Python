# Utilise une image légère de Python 3.10
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Variables d’environnement nécessaires au fonctionnement de l’API
ENV PROJECT_ID="mini-api-459410"
ENV REGION="europe-west1"
ENV BUCKET_NAME="bucket-mini-api"
ENV FILE_NAME="data.json"

# Exposer le port utilisé par Flask
EXPOSE 8080

# Commande pour démarrer l'application
CMD ["python", "app.py"]
