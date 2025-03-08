🎯 Mini-Application Flask – Affichage des Compétences avec Animation

📌 Description

Cette mini-application Flask affiche une liste de compétences avec des barres de progression animées en JavaScript pur (sans jQuery).Chaque barre démarre à 0% et atteint progressivement la valeur définie, offrant une animation fluide et dynamique.


🛠️ Installation & Exécution (Sans Docker)

1️⃣ Cloner le projet

git clone https://github.com/ton-repo/mini-flask-skills.git
cd mini-flask-skills

2️⃣ Créer un environnement virtuel et installer Flask

python -m venv venv
source venv/bin/activate  # Sur macOS/Linux
venv\Scripts\activate     # Sur Windows
pip install flask

3️⃣ Lancer l’application

python app.py

📌 Ouvre un navigateur et va sur http://127.0.0.1:5000/skills 🚀

🐳 Déploiement avec Docker

1️⃣ Construire l’image Docker

Assurez-vous d’être dans le dossier du projet où se trouve le Dockerfile, puis exécutez :

docker build -t my_app .

2️⃣ Lancer le conteneur

docker run -p 5000:5000 my_app

L’application sera accessible sur http://127.0.0.1:5000 🚀
