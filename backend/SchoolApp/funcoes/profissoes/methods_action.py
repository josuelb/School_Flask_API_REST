from db.db_connection import *


def response_profissoes():
    my_cursor.execute('SELECT * FROM profissoes')
    data = my_cursor.fetchall()

    profissoes = list()
    for d in data:
        profissoes.append(
            {
                "id": d[0],
                "name": d[1],
            }
        )
    return profissoes


def post_profissoes(d):
    my_cursor.execute(f'INSERT INTO profissoes VALUE {d}')
    my_cursor.execute('SELECT * FROM profissoes')


def delete_profissoes(idp):
    d = response_profissoes()
    dado = ''

    for i in d:
        if i['id'] == int(idp):
            dado = i

    my_cursor.execute(f'DELETE FROM profissoes WHERE id={dado["id"]}')