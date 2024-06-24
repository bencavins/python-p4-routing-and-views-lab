#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>", 200

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f"{param}", 200

@app.route('/count/<int:param>')
def count(param):
    result = ''
    for num in range(param):
        result += str(num) + '\n'
    return result, 200


@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2), 200
    elif operation == '-':
        return str(num1 - num2), 200
    elif operation == '*':
        return str(num1 * num2), 200
    elif operation == 'div':
        return str(num1 / num2), 200
    elif operation == '%':
        return str(num1 % num2), 200
    else:
        return f"Invalid operator: {operation}", 400
