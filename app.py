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
        number = int(request.form.get("search", 0))
        quant = int(request.form.get("elements", 10))

        if number >= quant:
            return render_template("error.html", message = "numero maior que a quantidade")

        dados = random.sample(range(0, quant), quant)

    return dados

def play():
    return


#{71, 46, 42, 96, 56, 60, 5, 75, 78, 90, 19}
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/bubblesort" , methods = ["POST" ,"GET"])
def bubblesort():

    get_elements()

    return render_template("bubblesort.html", dados = dados, quant = quant)

@app.route("/bubblesort/steps" , methods = ["GET"])
def bubblesort_step():
    global dados, quant

    quant = len(dados)

    #implementacao do algoritmo:
    steps = []

    for i in range(quant):
        for j in range(quant- i -1):
            if dados[j] > dados[j+1]:
                aux = dados[j+1]
                dados[j+1] = dados[j]
                dados[j] = aux

                steps.append(dados.copy())

    if steps is None:
        return jsonify({"error": "Nenhum dado encontrado"}), 404
    return jsonify(steps)

@app.route("/insertion", methods = ["POST" ,"GET"])
def insertion():

    get_elements()

    #implementacao do algoritmo:

    for i in range(1, quant):
        chave = dados[i]
        j = i - 1

        while j >= 0 and dados[j] > chave:
            dados[j+1] = dados [j]
            j-=1

        dados[j+1] = chave

    print(dados)

    return render_template("insertion.html")

@app.route("/selection", methods = ["POST" ,"GET"])
def selection():

    get_elements()

    for i in range(quant - 1):
        n_menor = i

        for j in range(i+1,quant):
            if dados[n_menor] > dados[j]:
                n_menor = j

        aux = dados[n_menor]
        dados[n_menor] = dados[i]
        dados[i] = aux

    print(dados)
    return render_template("selection.html")


@app.route("/merge", methods = ["POST" ,"GET"])
def merge():

    get_elements()

    #implementacao do algoritmo

    def merge_sort(arr): #divide ate ficar ordenado

        elements = len(arr)

        if elements <= 1:
            return arr

        mid = elements // 2

        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return juntar(left, right)

    def juntar(left, right):

        merge = []

        i = j = 0

        while len(left) > i and len(right) > j:
            if left[i] > right[j]:
                merge.append(right[j])
                j += 1
            elif left[i] < right[j]:
                merge.append(left[i])
                i += 1

        while len(left) > i:
            merge.append(left[i])
            i += 1

        while len(right) > j:
            merge.append(right[j])
            j += 1

        return merge

    dados[:] = merge_sort(dados)

    print(dados)

    return render_template("merge.html")

@app.route("/quick", methods = ["POST", "GET"])
def quick():

    get_elements()

    #implementacao do algoritmo:
    def sort(arr, left, right):

        if left < right:
            pi = partition(arr, left, right)
            sort(arr, left, pi-1)
            sort(arr, pi+1, right)

    def partition(arr, left, right):
        pi = arr[right]

        i = left-1

        for j in range(left, right):
            if arr[j] <= pi:
                i += 1
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux

        aux = arr[i+1]
        arr[i+1] = arr[right]
        arr[right] = arr[i+1]

        return i+1

    sort(dados, 0, quant - 1)

    print(dados)

    return render_template("quick.html")

@app.route("/linear", methods=["POST", "GET"])
def linear():
    get_search()

    for i in range(quant):
        if number == dados[i]:
            print("y", end='')
        else:
            print("n",end='')


    return render_template("linear.html")


@app.route("/binary", methods = ["POST", "GET"])
def binary():
    get_search()

    dados = list(range(quant))

    def search(arr, left, right):
        if left <= right:
            mid = (left + right)//2

            if arr[mid] == number:
                return mid

            elif number < arr[mid]:
                return search(arr, left, mid-1)

            elif number > arr[mid]:
                return search(arr, mid+1, right)

        return -1

    index = search(dados, 0, quant-1)

    if index == -1:
        print(f"numero; {number}, nao encontrado")
    else:
        print(f"numero: {number}, encontrado em {index}")


    return render_template("binary.html")


if __name__ == "__main__":
    app.run(debug=True)
