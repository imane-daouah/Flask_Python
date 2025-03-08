# Flask_Python_Docker 

## Description  
Ce projet est une mini-application Flask qui affiche une liste de **compétences** avec des **barres de progression animées en JavaScript pur** (sans jQuery). L'application est conteneurisée avec **Docker**, ce qui facilite son déploiement et son exécution dans un environnement isolé.

---

Fonctionnalités  
- **Affichage dynamique** des compétences à partir d’une liste Python.  
- **Animation fluide** des barres de progression en **JavaScript natif**.  
- **Utilisation de Flask & Jinja2** pour générer les pages dynamiquement.  
- **Structure de projet propre et bien organisée**.



Installation & Exécution

1. Cloner le projet
```bash
git clone https://github.com/imane-daouah/Flask_Python_Docker.git
```

2. Créer un environnement virtuel et installer Flask
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate     # Sur Windows
pip install -r requirements.txt
```
4. Lancer l’application localement
```bash
python app.py
```
Ouvre un navigateur et va sur 
```bash
http://127.0.0.1:5000 
```
Utilisation de Docker
Docker est utilisé pour conteneuriser cette application Flask. Suis les étapes ci-dessous pour créer l'image Docker et exécuter un conteneur.

1. Créer une image Docker
Dans le répertoire de ton projet, exécute la commande suivante pour créer une image Docker de l'application :
```bash
docker build -t flask_app .
```
Cette commande crée une image Docker appelée flask_app à partir du Dockerfile présent dans le répertoire du projet.

2. Lancer un conteneur Docker
Une fois l'image Docker créée, lance un conteneur basé sur cette image avec la commande suivante :
```bash
docker run -p 5000:5000 flask_app
```
Cette commande lance un conteneur avec le port local 5000 lié au port 5000 du conteneur Docker. L'application Flask sera alors accessible à l'adresse suivante dans ton navigateur :
http://127.0.0.1:5000

