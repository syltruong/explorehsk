from pathlib import Path
from typing import List

from collections import defaultdict
import fasttext
import numpy as np
import pandas as pd
from loguru import logger

from src.config import PATH_TO_FASTTEXT_BIN, PATH_TO_HSK_CSV, PROJECTOR_DATA_DIR, PATH_TO_SUBTLEX_CSV
from src.utils import pinyin_to_number_tones, score_occurence


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


def load_words(
    path_hsk_csv : Path = PATH_TO_HSK_CSV, 
    path_subtlex_csv: Path = PATH_TO_SUBTLEX_CSV
    ) -> pd.DataFrame:
    """
    Return a Chinese vocabulary dataframe

    Returns
    -------
    pd.DataFrame
        expected output columns are
        ["HSK Level", "Word", "Pronunciation_with_accents", "Definition", "Id", "Occurence"] 
    """

    df = pd.read_csv(path_hsk_csv)
    df_occurence = pd.read_csv(path_subtlex_csv)

    word_occurence = df_occurence.set_index("Word")["logW"].to_dict()

    df["level"] = df["level"].replace({"7-9" : "7"}, inplace=False).astype(int)
    df["Id"] = df["level"].astype(str) + "-" + df["num"].astype(str)
    in_cols = ["level", "simplified", "pinyin", "definitions", "Id"]
    out_cols = ["HSK Level", "Word", "Pronunciation_with_accents", "Definition", "Id"]
    
    df = df[in_cols].rename(columns=dict(zip(in_cols, out_cols)))
    df["Pronunciation"] = df["Pronunciation_with_accents"].apply(pinyin_to_number_tones)
    
    def _score_occurence(word):
        try:
            return score_occurence(word, word_occurence)
        except ValueError:
            return 0.0
    
    df["Occurence"] = df["Word"].apply(_score_occurence)
    
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
