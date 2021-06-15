from itertools import product

import pandas as pd
import pytest

from src.utils import (
    build_char_to_words,
    get_adj_words,
    generate_random_walk,
    WordGraphPathNotFoundException,
    pinyin_to_number_tones,
    score_occurence
)


def test_score_occurence():
    word_occurence = {
        "来" : 6, 
        "不" : 5,
        "对不起" : 4,
        "起来" : 3,
        "来自" : 2, 
    }

    words_to_score = ["对不起", "起来", "出来", "不客气"]
    expected_scores = [4, 3, 6, 5]

    for word, expected_score in zip(words_to_score, expected_scores):
        assert score_occurence(word, word_occurence) == expected_score

    with pytest.raises(ValueError):
        score_occurence("沿海", word_occurence)


def test_get_adj_words(words_series: pd.Series, occurence_series: pd.Series):
    word_id = 2
    
    expected_adj_words = list([4, 3, 1, 0])

    char_to_words = {
        "坚" : [0, 1, 2],
        "定" : [2, 3, 4]
    }

    adj_words = get_adj_words(
        word_id, 
        char_to_words=char_to_words, 
        words=words_series, 
        occurence=occurence_series
    )

    assert len(expected_adj_words) == len(adj_words)
    for val1, val2 in zip(expected_adj_words, adj_words):
        assert val1 == val2


def test_pinyin_to_number_tones():
    pinyin_with_accents = ["huí shǒu", "bèn dàn", "líng huó", "bà ba", "nǚ rén", "nǚ lu"]

    pinyin_with_numbers = ["hui2 shou3", "ben4 dan4", "ling2 huo2", "ba4 ba5", "nv3 ren2",  "nv3 lu5"]

    output = [pinyin_to_number_tones(word) for word in pinyin_with_accents]

    for out_word, expected_out_word in zip(output, pinyin_with_numbers):
        assert out_word == expected_out_word


def test_build_char_to_words(words_series: pd.Series):
    
    result_char_to_words = build_char_to_words(words_series)
    # expected_char_to_words = {
    #     "坚" : set(["坚果", "坚持", "坚定"]),
    #     "定" : set(["坚定", "决定", "肯定"]), 
    #     "果" : set(["坚果"]),
    #     "持" : set(["坚持"]),
    #     "决" : set(["决定"]),
    #     "肯" : set(["肯定"])
    # }
    expected_char_to_words = {
        "坚" : set([0, 1, 2]),
        "定" : set([2, 3, 4]), 
        "果" : set([0]),
        "持" : set([1]),
        "决" : set([3]),
        "肯" : set([4])
    }

    for key, value in result_char_to_words.items():
        assert expected_char_to_words[key] == value
    
    for key in expected_char_to_words.keys():
        assert key in result_char_to_words


# TODO: change the test to account for usage of word ids
# def test_generate_random_walk():
#     chars = list(range(10))
#     words = [f"{char1}{char2}" for char1, char2 in product(chars, repeat=2)]

#     char_to_words = build_char_to_words(words)

#     walk = generate_random_walk(char_to_words, n_steps=4)

#     # 1. check the length of the random walk
#     assert len(walk) == 4
    
#     # 2. check that the link characters are not repeated
#     common_chars = []
#     for i in range(len(walk) - 1):
#         common_char = walk[i][0] if walk[i][0] in walk[i+1] else walk[i][1]
#         common_chars.append(common_char)

#     assert len(set(common_chars)) == (len(walk) - 1)


# def test_generate_random_walk_exception():
#     char_to_words = {str(i) : [f"{i}{i}"] for i in range(10)}

#     with pytest.raises(WordGraphPathNotFoundException):
#         _ = generate_random_walk(char_to_words, n_steps=4)
