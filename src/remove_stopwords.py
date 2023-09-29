from typing import List


def get_stopwords(path: str) -> List[str]:
    """Returns the list of stopwords. The file should contain
    one stopword per new line.
    """
    with open(path, "r") as infile:
        return infile.read().split("\n")


def filter_words(path2txt: str, path2stopwords) -> str:
    """Filtering our stopwords from a given text.
    The input should be cleaned from punctuation marks.
    All the words should be lower-cased separated by a space.
    """
    stopwords = set(get_stopwords(path2stopwords))
    with open(path2txt, "r") as infile:
        txt = infile.read().strip().split()
    return " ".join([e for e in txt if e not in stopwords])