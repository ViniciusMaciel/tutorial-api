from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def meotodo_principal():
    return "<p>Sou a rota principal da api!</p>"

@app.route("/novometodo")
def novo_metodo():
    return "<p>Sou um nova rota!</p>"

@app.route("/novometodo/<parametro>")
def metodo_com_parametro(parametro):
    return "<p>Eu recebo um parametro assim no Flask:"+parametro+"</p>"

@app.route("/metodopost",methods=['POST'])
def metodo_post():
    return "<p>Sou um Post!</p>"

@app.route("/metodopostparametro",methods=['POST'])
def metodo_post_params():
    parametros = request.json

    meuparametro = parametros["meuparametro"]

    return jsonify(parametroenviado = meuparametro)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)