import datetime
from logging import Formatter
from flask import Flask, render_template, request
from pymongo import MongoClient #to open up client side session

app = Flask(__name__)
client = MongoClient("mongodb+srv://admin:admin@cluster0.gj9mz.mongodb.net/test")
app.db = client.pepBlog

entries=[]

@app.route("/", methods=["GET", "POST"])
def home():
    print([e for e in app.db.entries.find({})])

    if request.method ==  "POST":
        newPostContent = request.form.get("content")
        formattedDate = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((newPostContent, formattedDate))
        app.db.entries.insert_one({"content":newPostContent, "date":formattedDate})

    entries_with_date = [
        (entry[0],
        entry[1],
        datetime.datetime.strptime(entry[1],"%Y-%m-%d").strftime("%b %d")
        )

        for entry in entries
    ]
    
    return render_template("home.html", entries=entries_with_date)