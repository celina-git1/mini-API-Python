
# Mini-API Flask avec Docker et GCP

## Rôles de chacun

- **Romain** : Déploiement Docker en local, création du fichier `README.md`.
- **Zoé** : Déployer sur GCP via Cloud Run.
- **Célina** : Créer le dépôt Git, `app.py` avec les routes (`GET /Hello`, `GET /status`, `GET /joke`, `GET /data`, `POST /data`) et `requirements.txt`.

## Test Docker en local

```bash
docker build -t mini-api .
docker run -p 5000:5000 mini-api
```

## Étapes pour faire fonctionner notre mini-API Flask en local avec GCP, Vertex AI et GCS

### 1. Configuration du projet GCP

- **Créer le projet GCP** : `mini-api-459410`
- **Activer les APIs nécessaires** :
  - Administrateur Cloud Storage for Firebase
  - Administrateur Compute Storage
  - Administrateur des objets Storage
  - Administrateur Vertex AI
  - Créateur d'objets Storage
  - Lecteur de l'environnement et des objets Storage

### 2. Création et configuration du compte de service

- **Créer un compte de service GCP**
- **Télécharger la clé JSON**
- **Attribuer les rôles nécessaires** :
  - Vertex AI User
  - Storage Object Viewer
  - Storage Object Admin

### 3. Création du Bucket Cloud Storage

- **Créer le bucket GCS** : `bucket-mini-api`
- **Déposer un fichier JSON** : `data.json`

### 4. Création de l'image Docker

- Écrire un `Dockerfile` pour packager notre API Flask
- Ajouter les dépendances dans `requirements.txt`
- Construire l’image Docker : `mini-api`

### 5. Test de l'API Flask en local avec Docker

- Lancer le conteneur Docker avec les variables d’environnement et le volume de la clé

## Déployer l'application en ligne et la rendre accessible via Google Cloud

### 1. Publier l'image Docker sur Docker Hub

- Créer un compte Docker Hub et se connecter :
  ```bash
  docker login
  ```

- Taguer l'image Docker :
  ```bash
  docker tag mini-api zabadie/mini-api:latest
  ```

- Pousser l'image vers Docker Hub :
  ```bash
  docker push zabadie/mini-api:latest
  ```

### 2. Déployer sur GCP via Cloud Run

- Créer un service dans **Cloud Run**
- Spécifier l’image Docker : `zabadie/mini-api:latest`
- Choisir la région : `europe-west1`

### 3. Accéder à l'URL de notre application

- Une URL publique sera générée par Cloud Run pour accéder à notre API Flask.
- **[➡️ Lien vers la route /joke de l'API](https://mini-api-981015328293.europe-west1.run.app/joke)**

## 🔍 Exemple de résultats

### Accès à `/hello`

![Hello](https://raw.githubusercontent.com/celina-git1/mini-API-Python/main/image%20(3).png)

### Résultat de la route `/joke`

![Joke](https://raw.githubusercontent.com/celina-git1/mini-API-Python/main/image%20(1).png)

### Résultat de la route `/data`

![Data](https://raw.githubusercontent.com/celina-git1/mini-API-Python/main/image%20(2).png)

### Déploiement via Cloud Run

![Cloud Run](https://raw.githubusercontent.com/celina-git1/mini-API-Python/main/image.png)









