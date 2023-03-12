#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<parameter>')
def count(parameter):
    num = int(parameter)
    return '\n'.join([str(x) for x in range(num)]) + '\n'

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
