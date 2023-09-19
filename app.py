from flask import Flask

app = Flask(__name__)
@app.route("/")
 
def hello():
    print("hello")
 
@app.route("/add/<num1>/<num2>")
def div (num1,num2):
    return num1/num2