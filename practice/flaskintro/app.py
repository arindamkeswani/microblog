# python -m venv .venv
# source .venv/Scripts/activate
# pip install Flask
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run

from flask import Flask 
#flask class from flask package

app = Flask(__name__) #dunder name, always unique

#telling the app to register the end point
@app.route("/") 
def hello_world():
    return "Hello, developer!"

#will give error
@app.route("/hello") 
def hello_page():
    return "Hello page!"

@app.route("/webpage") 
def hello_html():
    return """
        <html>
            <body>
                <h1>Greetings!</h1>
                <p>paragraph<p>
            </body>
        </html>
    """