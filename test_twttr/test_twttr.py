from twttr import shorten

def test_spaced():
    assert shorten("Hello CS50 staff") == "Hll CS50 stff"
    assert shorten("What's up?") == "Wht's p?"
    assert shorten ("I'm Daniel") == "'m Dnl"


def test_oneword():
    assert shorten("Hello") == "Hll"
    assert shorten("World") == "Wrld"
    assert shorten("Python") == "Pythn"

