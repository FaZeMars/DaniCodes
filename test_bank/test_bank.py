from bank import value

def test_0():
    assert value("HeLlO") == 0
    assert value("helLO") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_20():
    assert value("HEY") == 20
    assert value("hEY") == 20
    assert value("hey there!") == 20
    assert value("howdy") == 20

def test_100():
    assert value("What's up?") == 100
    assert value("Good morning my friend!") == 100
    assert value("My guy!") == 100
