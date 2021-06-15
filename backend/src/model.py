from collections import defaultdict
from typing import Any, Dict, Optional

import numpy as np
import pandas as pd
from loguru import logger

from src.utils import build_char_to_words, get_adj_words 

class Model(object):
    def __init__(self, words_df: pd.DataFrame):
        """

        Parameters
        ----------
        words_df : pd.DataFrame
            the expected columns as 'Word', 'Pronunciation', 'Pronunciation_with_accents', 'Definition', 'Occurence'
            with a 'Id' index
        """

        # so that fields are in native Python type
        self.words_df = words_df.astype(object)

        self.char_to_words = build_char_to_words(words_df["Word"])

        logger.debug("Get HSK index lists")
        # each list contains the words of that level and below
        # ie. 4 : [all words of level 4 and below]
        
        max_hsk_level = words_df["HSK Level"].max()
        self.hsk_to_idx = defaultdict(list)
        for idx, hsk_level in enumerate(words_df["HSK Level"]):
            for l in range(hsk_level, max_hsk_level + 1):
                self.hsk_to_idx[l].append(idx)


    def ping(self):
        return f"I am alive with {len(self.word_to_idx)} words."


    def random(self, top: int = 20, hsk_level: Optional[int] = None) -> Dict[str, Any]:

        words_sub_df = self.words_df

        if hsk_level is not None:
            words_sub_df = words_sub_df.loc[words_sub_df["HSK Level"] <= hsk_level]
        
        sample_id = words_sub_df.sample(1).index.values[0]

        return self.get_similar_from_id(sample_id, top=top, hsk_level=hsk_level)


    def get_similar_from_id(self, word_id: str = None, top: int = 20, hsk_level: Optional[int] = None) -> Dict[str, Any]:

        word = self.words_df["Word"].loc[word_id]

        adj_word_ids = get_adj_words(
            word=word, 
            char_to_words=self.char_to_words, 
            occurence=self.words_df["Occurence"], 
            word_id=word_id
        )

        adj_words = self.words_df.loc[adj_word_ids]

        # level filtering
        if hsk_level is not None:
            adj_words = adj_words.loc[adj_words["HSK Level"] <= hsk_level]

        # top filtering
        adj_words = adj_words.iloc[:top]

        response = {
            "source": self.words_df.loc[word_id].to_dict("records"),
            "most_similar": adj_words.reset_index().to_dict("records"),
        }

        return response
