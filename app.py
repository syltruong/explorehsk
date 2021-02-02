from flask import Flask, jsonify

from src.init import load_words
from src.model import Model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

model = Model(load_words())

@app.route("/")
def hello_world():
    return jsonify(model.random())

@app.route("/other")
def other():
    return jsonify(model.get_similar("学习"))