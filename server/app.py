#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:n>')
def count(n):
    return '\n'.join([str(x) for x in range(n)]) + '\n'

@app.route('/math/<int:n1><string:op><int:n2>')
def math(n1, op, n2):
    if op == '+':
        return f'{n1 + n2}'
    elif op == '-':
        return f'{n1 - n2}'
    elif op == '*':
        return f'{n1 * n2}'
    elif op == '-':
        return f'{n1 - n2}'
    elif op == 'div':
        return f'{n1 / n2}'
    elif op == '%':
        return f'{n1 % n2}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
