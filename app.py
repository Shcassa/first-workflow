from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html', result=None)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}!")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        op = request.form['operation']

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            result = "Invalid operation"
    except Exception as e:
        result = f"Error: {e}"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run()



