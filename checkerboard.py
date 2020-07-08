from flask import Flask, render_template
import math
app = Flask(__name__)

@app.route("/")
def display8x8():
    return render_template("index.html", x=8, y=8)

@app.route("/<num>")
def displayGrid(num):
    x = int(num)
    y = int(num)
    return render_template("index.html", x=x, y=y)

@app.route("/<x>/<y>")
def displayXY(x, y):
    x = int(x)
    y = int(y)
    return render_template("index.html", x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)