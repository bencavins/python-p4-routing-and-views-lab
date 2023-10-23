#!/usr/bin/env python3

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    body = '<h1>Python Operations with Flask Routing and Views</h1>'
    return body, 200

@app.route('/print/<param>')
def print_string(param):
    print(param)
    return make_response(param, 200)

@app.route('/count/<int:x>')
def count(x):
    body = ''
    for num in range(0, x):
        body += f'{num}\n'
    return body, 200

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        body = num1 + num2
    elif operation == '-':
        body = num1 - num2
    elif operation == '*':
        body = num1 * num2
    elif operation == 'div':
        body = num1 / num2
    elif operation == '%':
        body = num1 % num2
    else:
        body = ''
    return str(body), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
