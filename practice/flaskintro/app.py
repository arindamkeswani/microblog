# python -m venv .venv
# source .venv/Scripts/activate
# pip install Flask
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

from flask import Flask, render_template
from jinja2 import Template
#flask class from flask package

app = Flask(__name__) #dunder name, always unique

#telling the app to register the end point
# @app.route("/") 
# def hello_world():
#     return render_template(
#         "jinja_intro.html",
#         name="Arindam",
#         language_name = "Jinja2")

# #will give error
# @app.route("/hello") 
# def hello_page():
#     return "Hello page!"

# @app.route("/webpage") 
# def hello_html():
#     return render_template("index2.html")

@app.route("/expressions/")
def expressions():

    #interpolation
    name="Steve"
    language_name = "Jinja2"

    #Addition, subtraction
    no_of_oranges=5
    no_of_apples=7
    old_quantity=9
    new_quantity=4
    first_name="Tony"
    last_name = "Stark"


    # return render_template("jinja_intro.html",
    #                         name=name,
    #                         language_name=language_name,
    #                         no_of_oranges=no_of_oranges,
    #                         no_of_apples=no_of_apples,
    #                         old_quantity=old_quantity,
    #                         new_quantity=new_quantity,
    #                         first_name=first_name,
    #                         last_name=last_name)

    kwargs = {
        "name":name,
        "language_name":language_name,
        "no_of_oranges":no_of_oranges,
        "no_of_apples":no_of_apples,
        "old_quantity":old_quantity,
        "new_quantity":new_quantity,
        "first_name":first_name,
        "last_name":last_name
    }

    return render_template("jinja_intro.html", **kwargs)