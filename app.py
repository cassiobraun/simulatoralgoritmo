from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

dados = []
quant = 10
number = 0

def get_elements():
    global dados, quant

    if request.method == "POST":
        quant = int(request.form.get("elements", 10))
    dados = random.sample(range(0, quant), quant)

def get_search():
    global dados, quant, number

    if request.method == "POST":
        quant = int(request.form.get("elements", 10))
        number = int(request.form.get("search", 0))

    dados = list(range(quant))

    return dados


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bubblesort" , methods = ["POST" ,"GET"])
def bubblesort():

    get_elements()

    return render_template("bubblesort.html", dados = dados, quant = quant)



@app.route("/insertion", methods = ["POST" ,"GET"])
def insertion():

    get_elements()

    return render_template("insertion.html", dados = dados, quant = quant)

@app.route("/selection", methods = ["POST" ,"GET"])
def selection():

    get_elements()

    return render_template("selection.html", dados = dados, quant = quant)


@app.route("/merge", methods = ["POST" ,"GET"])
def merge():

    get_elements()

    return render_template("merge.html", dados= dados, quant = quant)

@app.route("/quick", methods = ["POST", "GET"])
def quick():

    get_elements()

    return render_template("quick.html", dados = dados, quant = quant)

@app.route("/linear", methods=["POST", "GET"])
def linear():
    get_search()

    return render_template("linear.html", dados = dados, quant = quant, number = number)


@app.route("/binary", methods = ["POST", "GET"])
def binary():
    get_search()

    return render_template("binary.html", dados = dados, quant = quant, number = number)


if __name__ == "__main__":
    app.run(debug=True)