from loguru import logger

TONE_ACCENTS = {
    1 : "\u0304",
    2 : "\u0301",
    3 : "\u030C",
    4 : "\u0300",
    5 : "\u0307",
}

PINYIN_V = "u" + "\u0308"

VOWELS = ["a", "e", "i", "o", "u", "v"]

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
