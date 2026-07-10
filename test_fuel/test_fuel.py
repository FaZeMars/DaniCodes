from fuel import convert
from fuel import gauge
import pytest

#Test for convert function
def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        for number in ["0/4", "0/0", "0/100"]:
            assert convert(number) == ZeroDivisionError

def test_convert_string():
   with pytest.raises(ValueError):
        for string in ["one/3", "3/four", "one/4"]:
            assert convert(string) == ValueError

def test_convert_xgreaterthany():
   with pytest.raises(ValueError):
        for number in ["4/3", "8/4", "2/1"]:
            assert convert(number) == ValueError

def test_convert_xnegative():
    with pytest.raises(ValueError):
        for number in ["-3/3", "-4/2", "-10/100"]:
            assert convert(number) == ValueError


#Test for gauge function
def test_gauge_99():
    assert gauge(99) == "F"

def test_gauge_0():
    assert gauge(1) == "E"

def test_gauge_middle():
    for percent in [55, 67, 94, 9]:
        assert gauge(percent) == f"{percent}%"
