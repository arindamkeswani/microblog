import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

entries=[]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method ==  "POST":
        newPostContent = request.form.get("content")
        formattedDate = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((newPostContent, formattedDate))
    return render_template("home.html", entries=entries)