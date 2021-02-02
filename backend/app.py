from pathlib import Path
import pickle

from src.model import Model
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

root_path = Path(__file__).parent.absolute()

with open(root_path / "data" / "model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/ping")
def ping():
    return jsonify({"response": "I am alive!"})

@app.route("/random")
def random():
    return jsonify(model.random())

@app.route("/search")
def search():
    return jsonify(model.get_similar("学习"))