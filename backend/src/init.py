from typing import List

from collections import defaultdict
import fasttext
import numpy as np
import pandas as pd
from loguru import logger

from src.config import PATH_TO_FASTTEXT_BIN, PATH_TO_HSK_CSV, PROJECTOR_DATA_DIR


def get_ft_model():
    logger.debug("Load fasttext model")
    ft = fasttext.load_model(PATH_TO_FASTTEXT_BIN.as_posix())
    return ft


def get_embeddings(
    ft_model, words_list: List[str], etymologic: bool = False
) -> np.ndarray:

    logger.debug(f"Use etymologic: {etymologic}")

    out_embeddings = np.zeros(
        (len(words_list), ft_model.get_dimension()), dtype=np.float32
    )

    logger.debug("Begin get embeddings...")
    if etymologic:
        char_to_words = get_char_to_words_map(words_list)
        char_embeddings = get_char_embeddings(ft_model, char_to_words)

    for i, word in enumerate(words_list):
        if etymologic:
            out_embeddings[i, :] = np.mean(
                [char_embeddings[char] for char in word], axis=0
            )
        else:
            out_embeddings[i, :] = ft_model.get_word_vector(word)

    logger.debug(f"Return embeddings of shape {out_embeddings.shape}")
    return out_embeddings.astype(np.float32)


def get_char_to_words_map(words_list: List[str]):
    char_to_words = defaultdict(list)

    for word in words_list:
        for char in word:
            char_to_words[char].append(word)

    return char_to_words


def get_char_embeddings(ft_model, char_to_words):
    char_embeddings = {
        char: np.mean([ft_model.get_word_vector(word) for word in words], axis=0)
        for char, words in char_to_words.items()
    }
    return char_embeddings


def load_words() -> pd.DataFrame:
    df = pd.read_csv(PATH_TO_HSK_CSV)
    
    columns = ["Word", "Pronunciation", "Definition"]
    if "HSK Level" in df.columns:
        columns.append("HSK Level")

    df = df[columns]
    
    return df


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
