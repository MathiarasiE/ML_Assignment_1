from flask import Flask, render_template, request
from finds import train_finds, predict

app = Flask(__name__)

# Train model
hypothesis, attributes = train_finds("emails.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        promo = request.form["promo"]
        links = request.form["links"]
        sender = request.form["sender"]
        caps = request.form["caps"]

        input_data = [promo, links, sender, caps]

        result = predict(hypothesis, attributes, input_data)

    return render_template(
    "index.html",
    result=result,
    promo=promo if request.method=="POST" else "",
    links=links if request.method=="POST" else "",
    sender=sender if request.method=="POST" else "",
    caps=caps if request.method=="POST" else ""
)


if __name__ == "__main__":
    app.run(debug=True)
