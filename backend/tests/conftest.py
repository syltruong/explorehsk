import pandas as pd
import pytest


@pytest.fixture
def words_series() -> pd.Series:
    
    words = ["坚果", "坚持", "坚定", "决定", "肯定"]

    return pd.Series(
        data=words,
        index=list(range(len(words)))
    )


@pytest.fixture
def occurence_series(words_series) -> pd.Series:

    return pd.Series(
        data=[float(i) for i in range(len(words_series))],
        index=words_series.index
    )


@pytest.fixture
def words_df() -> pd.DataFrame:

    words = ["坚果", "坚持", "坚定", "决定", "肯定", "好", "好", "累", "累"]
    pronunciations = ["jian1guo3", "jian1chi2", "jian1ding4", "jue2ding4", "ken3ding4", "hao3", "hao3", "lei4", "lei2"]
    definitions = ["nut", "continue", "stable", "decide", "for sure", "good 1", "good 2", "tired", "accumulate"]
    hsk_levels = [3, 3, 4, 4, 2, 1, 2, 3, 4]

    return pd.DataFrame(
        data={
            "Word" : words, 
            "Pronunciation" : pronunciations, 
            "Definition" : definitions,
            "HSK_Level" : hsk_levels
        },
    )
