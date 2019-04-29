import os.path
from flask import Flask
app = Flask(__name__)

def root_dir():  
    return os.path.abspath(os.path.dirname(__file__))

@app.route("/")
def hello():
    return "Hello World!" 
@app.route("/index.html")
def index():
    return test.html