import argparse
from loguru import logger
import pickle
from pathlib import Path

from src.data import dedup_entries
from src.init import load_words
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
    words_df = dedup_entries(words_df)

    model = Model(words_df)
    output_path = output_dir / "model.pkl"
    with open(output_path, "wb") as f:
        pickle.dump(model, f)
        logger.debug(f"Model dumped to {output_path}")