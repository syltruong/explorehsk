from typing import List

import fasttext
import numpy as np
import pandas as pd
from loguru import logger

from config import PATH_TO_FASTTEXT_BIN, PATH_TO_HSK_CSV, PROJECTOR_DATA_DIR


def get_ft_model():
    logger.debug("Load fasttext model")
    ft = fasttext.load_model(PATH_TO_FASTTEXT_BIN.as_posix())
    return ft


def get_embeddings(
    ft_model, words_list: List[str], etymologic: bool = False
) -> np.ndarray:
    out_embeddings = np.zeros(
        (len(words_list), ft_model.get_dimension()), dtype=np.float32
    )

    logger.debug("Begin get embeddings...")
    for i, word in enumerate(words_list):
        if etymologic:
            out_embeddings[i, :] = np.mean(
                [ft_model.get_word_vector(char) for char in word]
            )
        else:
            out_embeddings[i, :] = ft_model.get_word_vector(word)

    logger.debug(f"Return embeddings of shape {out_embeddings.shape}")
    return out_embeddings.astype(np.float32)


def main():
    df = pd.read_csv(PATH_TO_HSK_CSV)[["Word", "Pronunciation", "Definition"]]

    out_stem = PATH_TO_HSK_CSV.stem

    # load model
    ft_model = get_ft_model()

    # export embeddings
    embeddings = get_embeddings(ft_model, df["Word"])
    embeddings.tofile(PROJECTOR_DATA_DIR / f"{out_stem}_semantic.bytes")

    embeddings = get_embeddings(ft_model, df["Word"], etymologic=True)
    embeddings.tofile(PROJECTOR_DATA_DIR / f"{out_stem}_etymologic.bytes")

    # export labels
    df.to_csv(PROJECTOR_DATA_DIR / f"{out_stem}.tsv", sep="\t", index=False)


if __name__ == "__main__":
    main()
