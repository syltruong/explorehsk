from flask import Flask

from src.init import load_words
from src.model import Model

app = Flask(__name__)

model = Model(load_words())

@app.route("/")
def hello_world():
    return "Hello, World" + model.ping()