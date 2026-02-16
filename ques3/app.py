from flask import Flask, render_template, request
import pandas as pd
from finds import id3, predict

app = Flask(__name__)

data = pd.read_csv("buy_computer.csv")
attributes = ["Age", "Income", "Student", "CreditRating"]

tree = id3(data, attributes)

@app.route("/", methods=["GET","POST"])
def index():
    result = None

    if request.method == "POST":
        sample = {
            "Age": request.form["age"],
            "Income": request.form["income"],
            "Student": request.form["student"],
            "CreditRating": request.form["credit"]
        }
        result = predict(tree, sample)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
