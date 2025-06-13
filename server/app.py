#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(n) for n in range(number)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
@app.route('/math/<string:operation>/<int:num1>/<int:num2>')
def math(num1, operation, num2):
    # Handle case where operation comes first in URL
    if isinstance(num1, str):
        operation, num1 = num1, operation
    
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%' or operation == 'mod':
        return str(num1 % num2)
    else:
        return 'Operation not recognized. Please use one of the following: + - * div % mod'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
