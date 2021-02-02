import argparse
from loguru import logger
import pickle
from pathlib import Path

from src.init import load_words, get_ft_model, get_embeddings
from src.model import Model


if __name__ == "__main__":
    # Build a model and pickle dump it somewhere

    parser = argparse.ArgumentParser(
        description="Build a word similiarity model and pickle dump it"
    )
    parser.add_argument("output_dir", type=str, help="output dir")

    args = parser.parse_args()
    output_dir = Path(args.output_dir)

    words_df = load_words()

    ft = get_ft_model()
    logger.debug("Get embeddings")
    embeddings = get_embeddings(ft, words_df["Word"])    

    model = Model(words_df, embeddings)
    output_path = output_dir / "model.pkl"
    with open(output_path, "wb") as f:
        pickle.dump(model, f)
        logger.debug(f"Model dumped to {output_path}")