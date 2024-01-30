from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder="templates")


# Métodos http
# GET: Obtener datos
# POST: Crear datos
# PUT: Actualizar datos
# DELETE: Eliminar datos


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route("/hello")
def hello():
    return "Hello, World desde otra ruta!"


@app.route("/hello_template")
def hello_template():
    lista = [
        {"num": 1, "visible": True},
        {"num": 2, "visible": False},
        {"num": 3, "visible": True},
    ]
    return render_template("ejemplo.html", nombre="Juan", lista=lista)


@app.route("/hello_template/<nombre>")
def hello_template_nombre(nombre):
    return render_template("ejemplo_parametro.html", nombre=nombre)

@app.route("/obtener_lista")
def obtener_lista():
    lista = [
        {"num": 1, "visible": True},
        {"num": 2, "visible": False},
        {"num": 3, "visible": True},
    ]
    return jsonify(lista)


if __name__ == "__main__":
    app.run(debug=True)
