from src.utils import build_word_graph


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
