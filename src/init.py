from typing import List

import fasttext
import numpy as np
import pandas as pd
from loguru import logger

from config import PATH_TO_FASTTEXT_BIN, PATH_TO_HSK_CSV, PROJECTOR_DATA_DIR


def get_embeddings(words_list: List[str]) -> np.ndarray:
    logger.debug("Load fasttext model")
    ft = fasttext.load_model(PATH_TO_FASTTEXT_BIN.as_posix())

    out_embeddings = np.zeros((len(words_list), ft.get_dimension()), dtype=np.float32)

    logger.debug("Begin get embeddings...")
    for i, word in enumerate(words_list):
        out_embeddings[i, :] = ft.get_word_vector(word)

    logger.debug(f"Return embeddings of shape {out_embeddings.shape}")
    return out_embeddings


def main():
    df = pd.read_csv(PATH_TO_HSK_CSV)[["Word", "Pronunciation", "Definition"]]

    out_stem = PATH_TO_HSK_CSV.stem

    # export embeddings
    embeddings = get_embeddings(df["Word"]).astype(np.float32)
    embeddings.tofile(PROJECTOR_DATA_DIR / f"{out_stem}.bytes")

    # export labels
    df.to_csv(PROJECTOR_DATA_DIR / f"{out_stem}.tsv", sep="\t", index=False)


if __name__ == "__main__":
    main()
