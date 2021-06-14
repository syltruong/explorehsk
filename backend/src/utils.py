from collections import defaultdict
import random
import unicodedata

from loguru import logger

TONE_ACCENTS = {
    1 : "\u0304",
    2 : "\u0301",
    3 : "\u030C",
    4 : "\u0300",
    5 : "\u0307",
}

TWO_DOTS_ACCENT = "\u0308" 
PINYIN_V = "u" + TWO_DOTS_ACCENT

VOWELS = ["a", "e", "i", "o", "u", "v"]

MAX_RANDOM_WALK_ATTEMPTS = 10


def add_pinyin_accents(pinyin: str) -> str:
    """
    Implement rules from http://www.pinyin.info/rules/where.html

    Parameters
    ----------
    pinyin : str
        plain pinyin with no accents and numbers at the end of each character, 
        ie "nv3 peng2 you3", "xing4 fu3"
    """

    out_chars = []

    for char in pinyin.split(" "):

        try:
            tone = int(char[-1])
        except ValueError as e:
            logger.warning(e)
            logger.warning(f"error on character: {char}")
            logger.warning(f"will return as is")
            out_chars.append(char)
            continue

        char = char[:-1]
        
        # check for presence of "a" and "e"
        if ("a" in char) or ("e" in char):
            char = char.replace("a", "a" + TONE_ACCENTS[tone])
            char = char.replace("e", "e" + TONE_ACCENTS[tone])
            char = char.replace("v", PINYIN_V)
            out_chars.append(char)
            continue
        
        # check for presence of "ou"
        if "ou" in char:
            char = char.replace("o", "o" + TONE_ACCENTS[tone])
            char = char.replace("v", PINYIN_V)
            out_chars.append(char)
            continue
        
        # check for the last vowel
        for letter in char[::-1]:
            if letter in VOWELS:
                char = char.replace(letter, letter + TONE_ACCENTS[tone])
                char = char.replace("v", PINYIN_V)
                out_chars.append(char)
                break
    
    return " ".join(out_chars)


def _strip_accents(s: str):
    
    ret = []
    
    for char_pinyin in unicodedata.normalize('NFD', s).split(" "): 
        if TWO_DOTS_ACCENT in char_pinyin:
            char_pinyin = char_pinyin.replace("u", "v")
        
        ret.append(
            ''.join(c for c in char_pinyin if unicodedata.category(c) != "Mn")
            )

    return " ".join(ret)


def pinyin_to_number_tones(pinyin: str) -> str:
    """
    Convert an accented pinyin string to a pinyin string
    with numerals to indicate tone.

    Parameters
    ----------
    pinyin : str
        pinyin string with accents

    Returns
    -------
    str
        pinyin string with numbers instead of accents
    """

    words = pinyin.split(" ")

    ret = []

    for word in words:
        # detect the accent and append the word to ret
        word_no_accent = _strip_accents(word)
        
        for tone, accent in TONE_ACCENTS.items():
            if accent in unicodedata.normalize("NFD", word):
                ret.append(f"{word_no_accent}{tone}")
                break
        else:
            ret.append(f"{word_no_accent}5")
    
    return " ".join(ret)


def _get_all_substrings(word: str, min_len: int=1):
    for j in range(len(word), min_len - 1, -1):
        yield j, [word[i:i+j] for i in range(0, len(word) - j + 1)]


def score_occurence(word: str, word_occurence: dict[str, float]) -> float:
    """
    Get an occurence score for a given input word.
    If the word is not found in the dict, try scoring the substrings, 
    from the longest ones to the shortest ones.

    Parameters
    ----------
    word : str
        word to score
    word_occurence : dict[str, float]
        dict of scores

    Returns
    -------
    float
        occurence score

    Raises
    ------
    ValueError
        when we could not score the word
    """

    for len_substr, substrs in _get_all_substrings(word):
        scores = []
        for substr in substrs:
            if substr in word_occurence:
                scores.append(word_occurence[substr])
    
        if len(scores) > 0:
            if len_substr > 1:
                return max(scores)
            else:
                return min(scores)
    
    raise ValueError(f"Could not score {word}")


def build_char_to_words(words: list[str]) -> dict[str, set[str]]:
    """
    Build graph of words.

    The output is a dict which keys are words and
    values are words that share exactly one common character

    Parameters
    ----------
    words : list[str]
        List of words

    Returns
    -------
    dict[str, list[str]]
        Graph of words
        Only words of exactly two characters are kept.
    """

    words = [word for word in words if len(word)==2]

    char_to_words = defaultdict(set)

    for word in words:
        for char in word:
            char_to_words[char].add(word)

    return char_to_words


def get_adj_words(word, char_to_words):
    
    ret = set().union(*[char_to_words[char] for char in word])
    ret.remove(word)

    return ret


def generate_random_walk(char_to_words: dict[str, set[str]], n_steps: int) -> list[str]:
    """
    Generate a random walk in the word graph.

    Parameters
    ----------
    word_graph : dict[str, list[str]]
        graph of words
    n_steps : int
        target number of steps in the random walk

    Returns
    -------
    list[str]
        list of word series
    """

    def _is_valid_candidate(word, past_words):
        for past_word in past_words:
            if word in get_adj_words(past_word, char_to_words):
                return False
        return True

    def _random_walk_from_start(start_word: str):
        # perform a DFS to find a path with the specified number of steps
        visited = []
        
        to_visit = [(start_word, 0)]
        ret = [start_word]
        
        while len(to_visit) > 0:
            
            word, rank = to_visit.pop(0)
            
            if word not in visited:
                visited.append(word)
                
                if rank < len(ret):
                    ret = ret[:rank]
            
                ret.append(word)

                if len(ret) >= n_steps:
                    return ret
                
                adj_words = [w for w in get_adj_words(word, char_to_words) if _is_valid_candidate(w, ret[:-1])]

                random.shuffle(adj_words)
                
                for adj_word in adj_words:
                    if adj_word not in visited:
                        to_visit.insert(0, (adj_word, rank+1))
        
        return None

    words = list(set().union(*char_to_words.values()))
    random.shuffle(words)

    for attempt in range(MAX_RANDOM_WALK_ATTEMPTS):

        start_word = words.pop()
        logger.info(f"attempt {attempt + 1}")
        logger.info(f"starting with word {start_word}")

        candidate_walk = _random_walk_from_start(start_word)

        if candidate_walk is not None:
            return candidate_walk
    
    raise WordGraphPathNotFoundException

class WordGraphPathNotFoundException(Exception):
    pass
