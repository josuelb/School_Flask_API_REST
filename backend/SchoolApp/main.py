from flask import Flask, request
from funcoes.alunos.methods_actions import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/alunos', methods=['GET', 'POST', 'DELETE'])
def get_app():
    if request.method == "GET":
        return response_alunos()
    elif request.method == "POST":
        body = request.json
        print(body)

        d = list()
        for b in body:
            d.append(
                (
                    b['id'],
                    b['nome'],
                    b['data_nasc'],
                    b['cpf']
                )
            )

        for post in d:
            post_alunos(post)
        return response_alunos()
    else:
        body = request.json

        delete_alunos(body['cpf'])
        return response_alunos()


app.run(debug=True)
