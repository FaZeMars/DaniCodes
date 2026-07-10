from fuel import convert
from fuel import gauge

def test_convert_zero():
    for number in ["0/4", "0/0", "0/100"]:
        assert convert(number) == ZeroDivisionError

def test_convert_string():
    for string in ["one/3", "3/four", "1/4"]:
        assert convert(string) == ValueError

def test_convert_xgreaterthany():
    for number in ["4/3", "8/4", "2/1"]:
        assert convert(number) == ValueError

def test_convert_xnegative():
    for number in ["-3/3", "-4/2", "-10/100"]:
        assert convert(number) == ValueError


