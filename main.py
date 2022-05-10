import os

from flask import Flask, request
from werkzeug.exceptions import BadRequest
from functions import *

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def build_query(f, cmd1, value1, cmd2, value2):
    f = map(lambda v: v.strip(), f)
    if cmd1 == '0' and cmd2 == '0':
        raise BaseException("Incorrect query")
    if cmd1 != '0':
        result = process_query(f, cmd1, value1)
        if cmd2 != '0':
            result = process_query(result, cmd2, value2)
    else:
        result = process_query(f, cmd2, value2)
    return result


@app.route("/perform_query")
def perform_query():
    try:
        cmd1 = request.args['cmd1']
    except KeyError:
        cmd1 = '0'
    try:
        value1 = request.args['value1']
    except KeyError:
        value1 = '0'
    try:
        cmd2 = request.args['cmd2']
    except KeyError:
        cmd2 = '0'
    try:
        value2 = request.args['value2']
    except KeyError:
        value2 = '0'
    try:
        file_name = request.args['file_name']
    except KeyError:
        raise BadRequest(description="File's name is required")

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return BadRequest(description=f'{file_name} was not found')

    with open(file_path) as f:
        result = build_query(f, cmd1, value1, cmd2, value2)
        content = '\n'.join(result)


    # получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
    # проверить, что файл file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
    # с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
    # вернуть пользователю сформированный результат
    return app.response_class(content, content_type="text/plain")


if __name__ == '__main__':
    app.run()
