from pathlib import Path
import pickle

from loguru import logger
from src.model import Model
from flask import Flask, jsonify, request
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

@app.route("/query")
def query():
    word = request.args.get('word')

    if word is not None:
        try:
            most_similar = model.get_similar(word)
            return jsonify(most_similar)
        except ValueError:
            return f'word {word} does not exist in vocab', 400 
    else:
        return 'Must provide argument `word`', 400
