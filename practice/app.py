import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method ==  "POST":
        newPostContent = request.form.get("content")
        formattedDate = datetime.datetime.today().strftime("%Y-%m-%d")
        print(newPostContent, formattedDate)
    return render_template("home.html")