# 1️⃣ Utilisation d'une image de base légère de Python 3.8
FROM python:3.9-slim

# 2️⃣ Définition du répertoire de travail dans le conteneur
WORKDIR /app

# 3️⃣ Copie du fichier requirements.txt dans le conteneur
COPY requirements.txt requirements.txt

# 4️⃣ Installation des dépendances Python listées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copie de tous les fichiers du projet local vers le conteneur
COPY . .

# 6️⃣ Commande de démarrage de l'application lorsque le conteneur est exécuté
CMD ["python", "app.py"]
 