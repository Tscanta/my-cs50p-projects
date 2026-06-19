#Implements the twttr.py program from WEEK 2

from twttr import shorten

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_numbers():
    assert shorten("123") == "123"


def test_punctuation():
    assert shorten("!?.,") == "!?.,"
