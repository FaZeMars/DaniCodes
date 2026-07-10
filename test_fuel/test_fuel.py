from fuel import convert
from fuel import gauge

def test_convert_zero():
    for number in ["0/4", "0/0", "0/100"]:
        assert convert(number) == ZeroDivisionError

def test_convert_string():
    for string in ["one/3", "3/four", "1/4"]:
        assert convert(string) == ValueError

def test_convert_x


