from flask import Flask


app = Flask(__name__)

"""
    Esto que estamos viendo acá con el @ es un decorator.

    Un decocrator es una forma de programar (Es un patrón de diseño)
    En escencia toma una función y le agrega cosas.
"""
@app.route('/')
def home():
    return 'Hola Mundo Flask'

"""
    Este if tambien es muy tipico de python.

    Lo que significa es que si yo ejecuto el script en una consola, osea:
    > python hello.py

    Por otro lado, si yo importo este modulo en otro archivo.py:
    import hello

    este if da falso y no se ejecuta.
"""
if __name__ == '__main__':
    app.run(debug=True)

