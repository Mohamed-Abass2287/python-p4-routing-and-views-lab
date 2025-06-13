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

@app.route('/count/<int:param>')
def count(param):
    # Join numbers with newline characters for correct test output.
    numbers = '\n'.join(str(num) for num in range(param))
    return numbers

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation in ['+', 'add']:
        result = num1 + num2
    elif operation in ['-', 'sub']:
        result = num1 - num2
    elif operation in ['*', 'mul']:
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2  # Division returns a float.
    elif operation in ['%', 'mod']:
        result = num1 % num2
    else:
        return 'Invalid operation'
    return str(result)

if __name__ == '__main__':
    app.run()
