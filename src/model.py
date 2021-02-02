import random
from typing import Any, Dict

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.metrics.pairwise import cosine_similarity

from src.init import get_embeddings, get_ft_model


class Model(object):
    def __init__(self, words_df: pd.DataFrame):
        """

        Parameters
        ----------
        words_df : pd.DataFrame
            the expected columns as 'Word', 'Pronunciation', 'Definition'
        """

        logger.debug("Load model")
        ft = get_ft_model()

        logger.debug("Get embeddings")
        self.embeddings = get_embeddings(ft, words_df["Word"])

        self.words_df = words_df
        self.word_to_idx = {word: idx for idx, word in enumerate(words_df["Word"])}

        logger.debug("Get distances")
        distances = cosine_similarity(self.embeddings, self.embeddings)
        self.sorted_idx = np.fliplr(np.argsort(distances, axis=1))
        self.sorted_distances = np.fliplr(np.sort(distances, axis=1))

    def ping(self):
        return f"I am alive with {len(self.word_to_idx)} words."

    def random(self, top: int = 10) -> Dict[str, Any]:

        random_idx = random.randint(0, len(self.word_to_idx) - 1)

        return self.get_similar_from_idx(random_idx, top=top)

    def get_similar(self, word: str, top: int = 10) -> Dict[str, Any]:

        if word not in self.word_to_idx:
            raise ValueError(f"Word not found in vocab list ({word})")

        word_idx = self.word_to_idx[word]

        return self.get_similar_from_idx(word_idx, top=top)

    def get_similar_from_idx(self, word_idx: int, top: int = 10) -> Dict[str, Any]:

        indices = self.sorted_idx[word_idx, :top]
        distances = self.sorted_distances[word_idx, :top]

        target_words = []
        for idx, distance in zip(indices, distances):
            target_words.append(
                {**self.words_df.iloc[idx].to_dict(), "distance": float(distance)}
            )

        response = {
            "source": self.words_df.iloc[word_idx].to_dict(),
            "most_similar": target_words,
        }

        return response
