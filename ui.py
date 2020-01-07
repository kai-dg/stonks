#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
import database as db
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    data = db.read()
    if request.method == "POST":
        to_add_list = ["ticker", "date_bought", "pb", "amt"]
        add = []
        for i in to_add_list:
            if request.form.get(i) == "":
                return "<h1>Could not add ticker.</h1>"
            else:
                add.append(request.form.get(i))
        # reference to database.py classes
        db.update(db.TickerSet(add[0].upper(), add[1], float(add[2]), int(add[3])))
        # TODO use api to update price here
        price = 999.98
        db.update(db.Price(add[0].upper(), price))
        data = db.read()
    return render_template("home.html", context=data)

@app.route("/api", methods=["GET"])
def api():
    return db.read()

if __name__ == "__main__":
    app.run(debug=True)
