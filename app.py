from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Greet API!'

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run()

