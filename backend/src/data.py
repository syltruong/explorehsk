import pandas as pd

def dedup_entries(words_df: pd.DataFrame) -> pd.DataFrame:
    """
    Deduplicate entries in the dataset,
    based on columns "Word" and "Pronunciation"

    The "HSK_Level" is set to the lowest level.
    The "Definition" is set to be the one of the lowest level.

    Parameters
    ----------
    words_df : pd.DataFrame
        words dataframe, the expected columns are
        "Word", "Pronunciation", "HSK_Level"

    Returns
    -------
    pd.DataFrame
        words dataframe with no duplicates
    """

    df = words_df.sort_values("HSK_Level")
    df = df.drop_duplicates(["Word", "Pronunciation"], keep="first")
    
    ret = words_df.loc[words_df.index.isin(df.index)]

    return ret
    