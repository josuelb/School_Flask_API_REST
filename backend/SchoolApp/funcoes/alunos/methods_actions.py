from db.db_connection import *


def response_alunos():
    my_cursor.execute('SELECT * FROM alunos')
    data = my_cursor.fetchall()

    alunos = list()
    for dado in data:
        alunos.append(
            {
                "id": dado[0],
                "nome": dado[1],
                "data_nasc": dado[2],
                "cpf": dado[3]
            }
        )
    return alunos


def post_alunos(d):
    my_cursor.execute(f'INSERT INTO alunos VALUE {d}')
    my_cursor.execute('SELECT * FROM alunos')


def delete_alunos(cpf):
    d = response_alunos()
    dado = ''

    for i in d:
        if i['cpf'] == int(cpf):
            dado = i

    my_cursor.execute(f'DELETE FROM alunos WHERE id={dado["id"]}')