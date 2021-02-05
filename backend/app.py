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
    top = request.args.get("top", default=20, type=int)
    hsk_level = request.args.get("hskLevel", default=None, type=int)

    random_suggestions = model.random(top=top, hsk_level=hsk_level) 
    
    return jsonify(random_suggestions)

@app.route("/query")
def query():
    word = request.args.get('word')
    top = request.args.get("top", default=20, type=int)
    hsk_level = request.args.get("hskLevel", default=None, type=int)

    if word is not None:
        try:
            most_similar = model.get_similar(word=word, top=top, hsk_level=hsk_level)
            return jsonify(most_similar)
        except ValueError:
            return f'word {word} does not exist in vocab', 400 
    else:
        return 'Must provide argument `word`', 400
