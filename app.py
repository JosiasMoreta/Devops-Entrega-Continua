from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return "Hola Mundo DevOps Estas en mi practica Josias Moreta🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)