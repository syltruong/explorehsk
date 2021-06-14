from itertools import product

import pytest

from src.utils import (
    build_word_graph,
    generate_random_walk,
    WordGraphPathNotFoundException,
    pinyin_to_number_tones
)

def test_pinyin_to_number_tones():
    pinyin_with_accents = ["huí shǒu", "bèn dàn", "líng huó", "bà ba", "nǚ rén", "nǚ lu"]

    pinyin_with_numbers = ["hui2 shou3", "ben4 dan4", "ling2 huo2", "ba4 ba5", "nv3 ren2",  "nv3 lu5"]

    output = [pinyin_to_number_tones(word) for word in pinyin_with_accents]

    for out_word, expected_out_word in zip(output, pinyin_with_numbers):
        assert out_word == expected_out_word


def test_build_word_graph():
    words = ["对不起", "对面", "面子", "幸福", "幸苦", "方面", "谢谢"]

    expected_graph = {
        "对面" : ["方面", "面子"],
        "面子" : ["方面", "对面"], 
        "幸福" : ["幸苦"],
        "幸苦" : ["幸福"],
        "方面" : ["对面", "面子"], 
        "谢谢" : []
    }

    result_graph = build_word_graph(words)

    for key, value in result_graph.items():
        assert set(expected_graph[key]) == set(value)
    
    for key in expected_graph.keys():
        assert key in result_graph


def test_generate_random_walk():
    chars = list(range(10))
    words = [f"{char1}{char2}" for char1, char2 in product(chars, repeat=2)]

    word_graph = build_word_graph(words)

    walk = generate_random_walk(word_graph, n_steps=4)

    # 1. check the length of the random walk
    assert len(walk) == 4
    
    # 2. check that the link characters are not repeated
    common_chars = []
    for i in range(len(walk) - 1):
        common_char = walk[i][0] if walk[i][0] in walk[i+1] else walk[i][1]
        common_chars.append(common_char)

    assert len(set(common_chars)) == (len(walk) - 1)


def test_generate_random_walk_exception():
    word_graph = {str(i) : [] for i in range(10)}

    with pytest.raises(WordGraphPathNotFoundException):
        _ = generate_random_walk(word_graph, n_steps=4)
