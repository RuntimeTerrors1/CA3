import flask from Flask

app = Flask(__name__)

@app("/")
def hello():
    print("Hello")

@app("/add/<num1>/<num2>")
def add(num1, num2):
    return num1+num2