from string import punctuation

EXCLUDE_CHARS = set(punctuation).union(set('’'))
def clean_text(text):
    for char in EXCLUDE_CHARS:
        text = text.replace(char, " ")
    return text.lower()

def simple_tokeniser(text):
    return text.split()