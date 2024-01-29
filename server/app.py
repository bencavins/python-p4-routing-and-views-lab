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

@app.route('/count/<int:num>')
def count(num):
    result = ""
    for x in range(0, num):
        result += str(x) + "\n"
    return result, 200

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
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
    else:
        return f"Invalid operation: {operation}", 404

    return str(result), 200


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)
