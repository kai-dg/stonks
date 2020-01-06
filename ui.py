#!/usr/bin/env python3
from flask import Flask
from flask import render_template
import database as db
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    data = db.read()
    return render_template("home.html", context=data)

@app.route("/api", methods=["GET"])
def api():
    return db.read()

if __name__ == "__main__":
    app.run(debug=True)
