#Implements the bank.py program from WEEK 1

from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("how are you") == 20


def test_other():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("123") == 100
