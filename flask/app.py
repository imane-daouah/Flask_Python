from flask import Flask, render_template  # Corriger l'import

# Initialisation de l'application Flask
skills_app = Flask(__name__)

my_skills = [("Html",80),("CSS",75),("Python",30)]


# Définition de la page d'accueil
@skills_app.route("/")
def homepage():
    return render_template("homepage.html", 
    pagetitle="Homepage",
    custom_css = "home")  # Corriger l'appel de la fonction

# Définition de la page "Add"
@skills_app.route("/add")
def add():
    return render_template("add.html", 
    pagetitle="Addpage",
    custom_css = "add")

# Définition de la page "About"
@skills_app.route("/about")
def about():
    return render_template("about.html", pagetitle="Aboutpage"  )

@skills_app.route("/skills")
def skills():
    return render_template("skills.html", pagetitle="My skills" ,
                           page_head = "My Skills" , 
                           description = "this is My Skilss Page",
                           skills = my_skills,
                           custom_css = "skills")

#dans les vraibles que je veux passe dans une page html Jinja2 ne lit pas tirer "-"
#page head et description sont de parametre paser ala page html skills.html et qui vont afciher dans cette page 


# Démarrage du serveur Flask si ce fichier est exécuté directement
if __name__ == "__main__":
    skills_app.run(debug=True)  # Active le mode debug
