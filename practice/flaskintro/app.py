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
@app.route("/") 
def hello_world():
    return render_template(
        "jinja_intro.html",
        name="Arindam",
        language_name = "Jinja2")

# #will give error
# @app.route("/hello") 
# def hello_page():
#     return "Hello page!"

# @app.route("/webpage") 
# def hello_html():
#     return render_template("index2.html")