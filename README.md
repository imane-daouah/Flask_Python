🎯 Mini-Application Flask – Affichage des Compétences avec Animation  

📌 Description  
Cette mini-application Flask affiche une **liste de compétences** avec des **barres de progression animées en JavaScript pur** (sans jQuery).  
Chaque barre démarre à **0%** et atteint progressivement la valeur définie, offrant une animation fluide et dynamique.  


🚀 Fonctionnalités  
✅ **Affichage dynamique** des compétences à partir d’une liste Python.  
✅ **Animation fluide des barres** de progression en **JavaScript natif**.  
✅ **Utilisation de Flask & Jinja2** pour générer les pages dynamiquement.  
✅ **Structure de projet propre et bien organisée**.  


🛠️ Installation & Exécution

1️⃣ Cloner le projet
```bash
git clone https://github.com/
cd flask
2️⃣ Créer un environnement virtuel et installer Flask
```bash
python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate     # Sur Windows
pip install flask
```
3️⃣ Lancer l’application
```bash
python app.py
```
📌 Ouvre un navigateur et va sur http://127.0.0.1:5000

🐳 Docker, Image et Conteneurisation
1️⃣ Qu'est-ce que Docker ?
Docker est une plateforme permettant de créer, exécuter et gérer des applications dans des conteneurs. Un conteneur est une unité légère et portable qui regroupe tout ce dont une application a besoin pour fonctionner (code, dépendances, configuration...).

2️⃣ Image Docker vs Conteneur
Image Docker 🖼️ : C'est un modèle ou un blueprint contenant tout le nécessaire pour exécuter une application (OS minimal, bibliothèques, code...).
Conteneur Docker 📦 : C'est une instance en cours d'exécution d'une image. Un conteneur peut être créé, démarré, arrêté et supprimé à tout moment.
3️⃣ Création de l'image Docker et exécution du conteneur

1️⃣ Créer une image Docker
Dans le répertoire de ton projet, crée une image Docker en utilisant la commande suivante :
```bash
docker build -t flask_app .
```
2️⃣ Lancer un conteneur à partir de l’image
Une fois l'image créée, tu peux lancer un conteneur à partir de cette image avec la commande suivante :
```bash
docker run -p 5000:5000 flask_app
```
3️⃣ Accéder à l’application
Ouvre ton navigateur et va sur l'URL suivante pour accéder à ton application Flask :
```bash
http://127.0.0.1:5000
```







