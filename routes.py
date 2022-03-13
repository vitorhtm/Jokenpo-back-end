from flask import Flask, request
from index import Jogo
from flask_cors import CORS

app = Flask("Hello world")
CORS(app)
jogo1 = Jogo()


@app.route("/jogar", methods=["POST"])
def jogar():
    body = request.get_json()
    return jogo1.jogar(body["jogada"])


app.run()
