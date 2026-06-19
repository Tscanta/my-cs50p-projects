#Implements the plates.py program from WEEK 2

from plates import is_valid

def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C550") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA222") == True


def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("CS,50") == False
    assert is_valid("HELLO!") == False

def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
