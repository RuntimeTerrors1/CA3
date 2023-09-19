from Flask import flask

app = Flask(__name__)

@app("/")
def hello():
    print("Hello")

@app("/add/<num1>/<num2>")
def add(num1, num2):
    return num1+num2
 
@app.route("/div/<num1>/<num2>")
def div (num1,num2):
    return num1/num2