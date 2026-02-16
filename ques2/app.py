from flask import Flask, render_template, request
from finds import best_income_split, predict

app = Flask(__name__)

threshold, gain = best_income_split("loan.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        income = float(request.form["income"])
        result = predict(income, threshold)

    return render_template("index.html", result=result,
                           threshold=threshold, gain=gain)

if __name__ == "__main__":
    app.run(debug=True)
