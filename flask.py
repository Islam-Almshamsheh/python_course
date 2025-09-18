# Flask looks for templates in the templates/ directory by default make sure to make yours in your working directory
#  debug=True in Flask, so templates reload on changes.
from flask import Flask, render_template
# render_template => allows you to add template in the root instead of returning strings there
skills_app = Flask(__name__) # giving our app a name

my_skills = [("html", 50), ("css",40), ("python",80), ("MySql",90), ("go",11)  ]

@skills_app.route("/")
def homepage():
    # return "Hello From Flask Framwork"
    # made an attribute (pagetitle) to control the html pages from the file itself (flask_133.py)
    return render_template("homepage.html", 
                            title="HomePage",
                            test="hello H",
                            custom_css="home")
@skills_app.route("/add")
def add():
    return render_template("add.html",
                            title="Addodi",
                            test=" Our Add Page =>",
                            custom_css="add")

@skills_app.route("/about")
def about():
    # return "About Page From Flask Framwork"
    return render_template("about.html",
                            title="About",
                            test="Hello A")

@skills_app.route("/skills")
def skills():
    return render_template("skills.html",
                            title="My Skills",
                            page_head="My Skills",
                            description="This Is My Skills Page",
                            skills=my_skills,
                            custom_css="skills")

# to run our application do the following
if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)

# The-flask-project
# ├── app.py (your Flask app)
# ├── templates/
# │   ├── base.html
# │   ├── homepage.html
# │   └── about.html
# ├── static/ ===> may has folder for js files and folder for images
# │   └── css/
# │       ├── main.css
# │       └── master.css
