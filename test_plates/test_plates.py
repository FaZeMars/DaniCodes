from plates import is_valid

def test_allnum():
    assert is_valid("111111") == False
    assert is_valid("010101") == False

def test_alfnum():
    assert is_valid("0SSDO3") == False
    assert is_valid("CS50") == True
    assert is_valid("COS500") == True
    assert is_valid("COS5000") == False
    assert is_valid("C") == False

def test_valid():
    for plate in ["CS50", "DAM300", "LIN251"]:
        assert is_valid("name") == True






