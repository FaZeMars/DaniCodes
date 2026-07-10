from plates import is_valid

def test_allnum():
    assert is_valid("111111") == "Invalid"
    assert is_valid("010101") == "Invalid"

def test_alfnum():
    assert is_valid("0SSDO3") == "Invalid"
    assert is_valid("CS50") == "Valid"
    assert is_valid("COS500") == "Valid"
    assert is_valid("COS5000") == "Invalid"
    assert is_valid("C5") == "Invalid"

def test_withspace():
    assert is

