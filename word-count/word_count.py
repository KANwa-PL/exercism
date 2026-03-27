import re
def count_words(sentence):
    result = {}
    pattern = r"(?<![^\W_])(?:[^\W\d_]+(?:['’][^\W\d_]+)*|\d)(?![^\W_])"
    for word in re.findall(pattern,sentence):
        result[word.lower()]= result.setdefault(word.lower(), 0) + 1
    return  result
