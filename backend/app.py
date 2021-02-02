from pathlib import Path
import pickle

from src.model import Model
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

root_path = Path(__file__).parent.absolute()

with open(root_path / "data" / "model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def hello_world():
    return jsonify(model.random())

@app.route("/other")
def other():
    return jsonify(model.get_similar("学习"))