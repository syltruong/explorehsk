import pandas as pd

from src.data import dedup_entries


def test_dedup_entries(words_df: pd.DataFrame):
    ret = dedup_entries(words_df)

    assert len(ret) == len(words_df) - 1
    assert len(ret.drop_duplicates(["HSK Level", "Word", "Pronunciation"])) == len(ret)
