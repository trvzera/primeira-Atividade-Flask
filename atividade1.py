from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print("O decorator é uma função \n E serve para acessar o caminho do Flask enviando para um caminho definido \nVocê digita @(nome da variavel instanciada com Flask).route('e o caminho aqui entre aspas') ")