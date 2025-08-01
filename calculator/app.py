from flask import Flask, request, jsonify, send_from_directory
from sympy import sympify, SympifyError, log, sqrt, zoo
from sympy.core.numbers import Number

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        result = float(data['a']) + float(data['b'])
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid number format'}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        result = float(data['a']) - float(data['b'])
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid number format'}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        result = float(data['a']) * float(data['b'])
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid number format'}), 400

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        a = float(data['a'])
        b = float(data['b'])
        if b == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = a / b
        return jsonify({'result': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid number format'}), 400


@app.route('/api/calculate')
def calculate():
    a = request.args.get('a')
    b = request.args.get('b')
    op = request.args.get('op')
    if a is None or b is None or op not in {'add', 'subtract', 'multiply', 'divide'}:
        return jsonify({'error': 'Invalid parameters'}), 400
    try:
        a_val = float(a)
        b_val = float(b)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400
    if op == 'add':
        result = a_val + b_val
    elif op == 'subtract':
        result = a_val - b_val
    elif op == 'multiply':
        result = a_val * b_val
    else:
        if b_val == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = a_val / b_val
    return jsonify({'result': result})


@app.route("/api/evaluate")
def evaluate():
    expr = request.args.get('expr')
    if not expr:
        return jsonify({"error": "Missing 'expr' parameter"}), 400

    try:
        # Define allowed functions for sympify
        allowed_locals = {
            "sqrt": sqrt,
            "log": log,
        }
        
        # Safely evaluate the expression
        # The expression is first parsed by sympify, then evaluated to a float.
        # locals are restricted to prevent arbitrary code execution.
        result = sympify(expr, locals=allowed_locals).evalf()

        # Check for infinity, which indicates division by zero
        if result in (zoo, -zoo):
            raise ZeroDivisionError

        # Ensure the result is a number, not a symbolic expression
        if not isinstance(result, Number) or result.has(zoo, -zoo):
            raise SympifyError("Invalid expression")

        return jsonify({"result": float(result)})

    except (SympifyError, TypeError):
        return jsonify({"error": "Invalid expression syntax"}), 400
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"}), 400
    except ValueError:
        return jsonify({"error": "Invalid value in expression"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
