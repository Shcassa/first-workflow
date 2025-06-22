from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('calculator.html', result=None)

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


