@skills_app.route("/skills")
def skills():
    return render_template("skills.html", pagetitle="My skills" ,
                           page_head = "My Skills" , 
                           description = "this is My Skilss Page",
                           skills = my_skills,
                           custom_css = "skills")
