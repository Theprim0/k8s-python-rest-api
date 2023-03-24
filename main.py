from flask import Flask, jsonify, make_response, request
import datetime
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello_world():

    # Obtenenos la hora
    hora = datetime.datetime.now()

    # Obtenemos la ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()

    # Obtenemos el nombre del host
    nombrePc = socket.gethostname()

    # Obtenemos el nombre del nodo
    nombreNodo = os.getenv("MY_NODE_NAME")

    if nombreNodo is None:
        print("WARN: Variable MY_NODE_NAME not specified, default to null")
        
    return make_response(jsonify(Hora=hora, IP=ip, Host=nombrePc, Nodo=nombreNodo), 200)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)