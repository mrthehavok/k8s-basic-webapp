from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)