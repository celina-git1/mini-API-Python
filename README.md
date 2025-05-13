Rôles de chacun

- Romain : Déploiement Docker en local,création du ficher README.md
- Zoé : Déployer sur GCP via Cloud Run
- Célina : Créér le dépôt Git, main.py avec (GET /Hello, GET /status, GET /joke,GET /data, POST /data requirements.txt)

Test Docker en local
- docker build -t mini-api .
- docker run -p 5000:5000 mini-api


Toute les étapes faites pour faire fonctionner notre mini-API Flask en local avec GCP, Vertex AI et GCS :

Configuration du projet GCP :
	- Créer le projet GCP : mini-api-459410
	- Activer les APIs nécessaires (Administrateur Cloud Storage for Firebase
Administrateur Compute Storage
Administrateur des objets Storage
Administrateur Vertex AI
Créateur d'objets Storage
Lecteur de l'environnement et des objets Storage)
 
Création et configuration du compte de service :
	- Créer un compte de service GCP
	- Télécharger la clé JSON 
	- Attribuer les rôles nécessaires (Vertex AI User, Storage Object Viewer et Storage Object Admin)
 
Création du Bucket cloud Storage :
	- Créer le bucket GCS : bucket-mini-api
	- Y déposer un fichier json: data.json
 
Au préalable créer le Dockerfile pour packager notre API Flask, ajouter les dépendances dans requirements.txt et constuire notre image Docker: mini-api .
 
 
Test de l'API Flask en local avec Docker:
	- Lancer notre conteneur Docker avec les variables d'environnement et le volume de la clé


Déployer l'application en ligne et la rendre accessible via Google Cloud :
 
Publier l'image Docker sur Docker Hub:
	- Créer compte Docker Hub, se connecter ( docker login )
	- Taguer notre image Docker ( docker tag mini-api zabadie/mini-api:latest )
	- Pousser l'image vers Docker Hub ( docker push zabadie/mini-api:latest )
 
Déployer sur GCP:
	- Créer un service dans Cloud Run en y spécifiant l'URL de notre image Docker Hub ( zabadie/mini-api:latest ) ainsi que la bonne région ( europe-west1 )
 
Accès à l'URL de notre application.


 