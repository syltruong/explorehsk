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
