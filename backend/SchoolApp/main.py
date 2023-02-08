from flask import Flask, request, redirect
from funcoes.alunos.methods_actions import *
from funcoes.funcionarios.methods_actions import *
from funcoes.profissoes.methods_action import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def home():
    return redirect('/alunos')


@app.route('/alunos', methods=['GET', 'POST', 'DELETE'])
def alunos():
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


@app.route('/funcionarios', methods=["GET", "POST", "DELETE"])
def funcionarios():
    if request.method == "GET":
        return response_funcionarios()
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
                    b['cpf'],
                    b['numero_inscricao'],
                    b['profissao_id']
                )
            )

        for post in d:
            post_alunos(post)
        return response_funcionarios()
    else:
        body = request.json

        delete_funcionario(body['n_inscricao'])
        return response_funcionarios()


@app.route('/profissões', methods=["GET", "POST", "DELETE"])
def profissoes():
    if request.method == "GET":
        return response_profissoes()
    elif request.method == "POST":
        body = request.json
        print(body)

        d = list()
        for b in body:
            d.append(
                (
                    b['id'],
                    b['nome']
                )
            )

        for post in d:
            post_profissoes(post)
        return response_profissoes()
    else:
        body = request.json

        delete_profissoes(body['id'])
        return response_profissoes()


app.run(debug=True)
