from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print("Hello")
    return "Hello, World!"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return str(num1 + num2)

@app.route("/div/<int:num1>/<int:num2>")
def div(num1, num2):
    try:
        result = num1 / num2
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"

@app.route("/mul/<int:a>/<int:b>")
def mul(a, b):
    return str(a * b)

if __name__ == "__main__":
    app.run(host="0.0.0.0")