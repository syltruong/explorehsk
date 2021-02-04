from collections import defaultdict
import random
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.metrics.pairwise import cosine_similarity


class Model(object):
    def __init__(self, words_df: pd.DataFrame, embeddings: np.array):
        """

        Parameters
        ----------
        words_df : pd.DataFrame
            the expected columns as 'Word', 'Pronunciation', 'Definition'
        """
        
        self.embeddings = embeddings

        # so that fields are in native Python type
        self.words_df = words_df.astype(object)
        self.word_to_idx = {word: idx for idx, word in enumerate(words_df["Word"])}

        logger.debug("Get HSK index lists")
        # each list contains the words of that level and below
        # ie. 4 : [all words of level 4 and below]
        
        max_hsk_level = words_df["HSK Level"].max()
        self.hsk_to_idx = defaultdict(list)
        for idx, hsk_level in enumerate(words_df["HSK Level"]):
            for l in range(hsk_level, max_hsk_level + 1):
                self.hsk_to_idx[l].append(idx)

        logger.debug("Get distances")
        distances = cosine_similarity(self.embeddings, self.embeddings)
        self.sorted_idx = np.fliplr(np.argsort(distances, axis=1))
        self.sorted_distances = np.fliplr(np.sort(distances, axis=1))

    def ping(self):
        return f"I am alive with {len(self.word_to_idx)} words."

    def random(self, top: int = 10, hsk_level: Optional[int] = None) -> Dict[str, Any]:

        if hsk_level is not None:
            random_idx = random.choice(self.hsk_to_idx[hsk_level])
        else:
            random_idx = random.randint(0, len(self.word_to_idx) - 1)

        return self.get_similar_from_idx(random_idx, top=top, hsk_level=hsk_level)

    def get_similar(self, word: str, top: int = 10, hsk_level: Optional[int] = None) -> Dict[str, Any]:

        if word not in self.word_to_idx:
            raise ValueError(f"Word not found in vocab list ({word})")

        word_idx = self.word_to_idx[word]

        return self.get_similar_from_idx(word_idx, top=top, hsk_level=hsk_level)

    def get_similar_from_idx(self, word_idx: int, top: int = 10, hsk_level: Optional[int] = None) -> Dict[str, Any]:

        indices = self.sorted_idx[word_idx, :]
        distances = self.sorted_distances[word_idx, :]

        # level filtering
        if hsk_level is not None:
            mask = np.isin(indices, self.hsk_to_idx[hsk_level])
            indices = indices[mask]
            distances = distances[mask]

        # top filtering
        indices =  indices[:top]
        distances =  distances[:top]

        target_words = []
        for idx, distance in zip(indices, distances):
            word_attributes = self.words_df.iloc[idx].to_dict() 
            target_words.append(
                {**word_attributes, "distance": float(distance)}
            )

        response = {
            "source": self.words_df.iloc[word_idx].to_dict(),
            "most_similar": target_words,
        }

        return response
