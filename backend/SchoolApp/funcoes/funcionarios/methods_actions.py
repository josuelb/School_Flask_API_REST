from db.db_connection import *


def response_funcionarios():
    my_cursor.execute('SELECT f.*, p.nome FROM funcionarios f LEFT OUTER JOIN profissoes p ON p.id_profissao=f.profissao')
    data = my_cursor.fetchall()

    funcionarios = list()
    for d in data:
        funcionarios.append(
            {
                "id": d[0],
                "name": d[1],
                "data_nasc": d[2],
                "cpf": d[3],
                "n_inscricao": d[4],
                "profissao": d[6]
            }
        )
    return funcionarios


def post_funcionario(d):
    my_cursor.execute(f'INSERT INTO funcinarios VALUE {d}')
    my_cursor.execute('SELECT * FROM funcionarios')


def delete_funcionario(n_inscricao):
    d = response_funcionarios()
    dado = ''

    for i in d:
        if i['numero_inscricao'] == int(n_inscricao):
            dado = i

    my_cursor.execute(f'DELETE FROM funcionarios WHERE id={dado["id"]}')
