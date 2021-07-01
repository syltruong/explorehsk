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


def get_comprehensive_pinyin_string_series(
    pinyin_with_accents : pd.Series, 
    pinyin_with_numbers : pd.Series
    ) -> pd.Series:
    """
    Get a pandas series of concatenated pinyin spellings

    Parameters
    ----------
    pinyin_with_accents : pd.Series
        pinyin series with accents
    pinyin_with_numbers : pd.Series
        pinyin series with numbers

    Returns
    -------
    pd.Series
        series of concatenated strings
    """


    res = pinyin_with_accents + " " + pinyin_with_numbers
    
    res = res + " " + pinyin_with_accents.apply(lambda pinyin : pinyin.replace(" ", ""))
    res = res + " " + pinyin_with_numbers.apply(lambda pinyin : pinyin.replace(" ", ""))

    res = res + " " + pinyin_with_numbers.apply(lambda pinyin : " ".join([elt[:-1] for elt in pinyin.split(" ")]))
    res = res + " " + pinyin_with_numbers.apply(lambda pinyin : "".join([elt[:-1] for elt in pinyin.split(" ")]))

    return res
    