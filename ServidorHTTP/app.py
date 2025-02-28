#flask para implementar el servidor y json para el formato (METODO GET)
from flask import Flask, request, jsonify
#para solicitudes api (METODO POST)
import requests

app = Flask(__name__)

# Endpoint GET 1: Mensaje simple
# Ruta: /
# Método: GET
# Respuesta: Mensaje de bienvenida
@app.route('/getObvio', methods=['GET'])
def home():
    return "Porque somos chavaAas"

# Endpoint GET 2: Información sobre el Modelo OSI
# Ruta: /data
# Método: GET
# Respuesta: Información sobre el Modelo OSI en formato JSON
@app.route('/getMicrobio', methods=['GET'])
def get_data():
    data = {
        "title": "Nombres",
        "description": ("Rosa Lizeth Suarez Medina y Valeria Paola Chavez Flores"),
        "quality": ("Nice")
    }
    return jsonify(data)

# Endpoint POST: Recibir y devolver datos
# Ruta: /api
# Método: POST
# Funcionalidad: Recibe datos en formato JSON y devuelve un mensaje de confirmación junto con los datos recibidos
@app.route('/post', methods=['POST'])
def api():
    data = request.get_json()
    return jsonify({"message": "POST successfully sent!", "data": data})

# Endpoint POST: Enviar solicitud POST a /api
# Ruta: /send_post
# Método: POST
# Funcionalidad: Envía una solicitud POST a la ruta /api con un payload JSON y devuelve la respuesta
@app.route('/send_post', methods=['POST'])
def send_post():
    url = "http://127.0.0.1:5000/api"
    payload = {"key": "value"}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return jsonify({"message": "Solicitud POST enviada a /api", "response": response.json()})
    else:
        return jsonify({"message": "Error al enviar solicitud POST", "status_code": response.status_code})

if __name__ == '__main__':
    app.run(debug=True)
