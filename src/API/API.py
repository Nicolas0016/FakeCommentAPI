from flask import Flask, jsonify
from fakeAPI import fake_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    headers = {
    'Content-Type': 'text/text-plain; charset="utf-8"',
    'Custom-Header': 'Faker API'
    }
    content = {
  "es": {
    "saludo": "Hola, y muchas gracias por usar mi generador de datos aleatorios",
    "elegir cantidad": "Para elegir la cantidad, debes agregar 'quantity' seguido del número deseado en la URL",
    "país": "Si deseas filtrar por un país específico, añade 'country' seguido del nombre del país en la URL",
    "clave valor": "Esta es una API de clave-valor, lo que significa que primero debes especificar el requerimiento y luego su valor",
    "concatenado": "Puedes concatenar tus requerimientos usando el símbolo '&' en la URL para agregar múltiples directivas"
  },
  "en": {
    "saludo": "Hello, and thank you very much for using my random data generator",
    "choose quantity": "To choose the quantity, you must add 'quantity' followed by the desired number in the URL",
    "country": "If you want to filter by a specific country, add 'country' followed by the country name in the URL",
    "key value": "This is a key-value API, which means you must first specify the requirement and then its value",
    "concatenated": "You can concatenate your requirements using the '&' symbol in the URL to add multiple directives"
  },"example":"/quantity=10"
}



    return jsonify(content), 200, headers



@app.route('/<string:URL>')
def get_link(URL):
    content = None

    params = URL.split("&")
    if params != []:
        country = ""
        quantity = 1
        headers = {
    'Content-Type': 'text/text-plain;charset="utf-8"',
    'Custom-Header': 'Faker API'
}
        for param in params:
            [specification, value] = param.split("=")
            if specification == "country":
                country = value
            elif specification == "quantity":
                quantity = int(value) 
        content = fake_api(quantity, country)

    return jsonify(content), 200, headers

if __name__ == '__main__':
    app.run(debug=True, port=400)
