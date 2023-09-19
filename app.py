from Flask import flask

app = Flask(__name__)

@app("/")
def hello():
    print ("Hello")

@app("/add/<a>/<b>")
def add(a, b):
    return a + b