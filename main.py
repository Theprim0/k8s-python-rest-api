from flask import Flask, jsonify, make_response, request
import datetime
import socket

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

    return make_response(jsonify(Hora=hora, IP=ip, Host=nombrePc), 200)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=80)