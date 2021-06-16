from src.init import load_words

def test_load_words():
    df = load_words()

    assert len(df) > 1
    
    expected_cols = ["HSK Level", "Word", "Pronunciation_with_accents", "Definition", "Occurence"]

    for col in expected_cols:
        assert col in df.columns
    
    assert df.index.name == "Id"
    