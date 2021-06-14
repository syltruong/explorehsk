from pathlib import Path
import pickle

from loguru import logger
from src.model import Model
from flask import Flask, json, jsonify, request
from flask_cors import CORS

from src.utils import (
    generate_random_walk, 
    WordGraphPathNotFoundException, 
    MAX_RANDOM_WALK_ATTEMPTS
)

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

@app.route("/new_game")
def new_game():
    # TODO: support filtering games according to HSK levels
    # hsk_level = request.args.get("hskLevel", default=None, type=int)
    n_steps = request.args.get("nSteps", default=4, type=int)

    try:
        walk = generate_random_walk(model.word_graph, n_steps=n_steps)
        return jsonify(
            {
                'start' : walk[0],
                'target' : walk[-1],
                'solution' : walk 
            }
        )
    except WordGraphPathNotFoundException:
        return f'Did not find a new game path after {MAX_RANDOM_WALK_ATTEMPTS} attempts'
