from numb3rs import validate

def test_words():
    assert validate("cat.penguin.bear.dog") == False
    assert validate("This.is.a.test") == False
    assert validate("How.are.you.doing") == False
    assert validate("This.is.CS50.Python") == False

def test_bigger():
    assert validate("257.277.296.67") == False
    assert validate("1.22.333.4444") == False
    assert validate("67.76.296.67") == False
    assert validate("1.11.111.1111") == False

def test_valid():
    assert validate("1.22.33.44") == True
    assert validate("0.0.0.0") == True
    assert validate("1.22.33.44") == True
    assert validate("255.255.255.255") == True

def test_nodot():
    assert validate("122.33.44") == False
    assert validate("0.0.00") == False
    assert validate("1.22.3344") == False
    assert validate("255.255255.255") == False
