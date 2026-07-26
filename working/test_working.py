from working import convert
import pytest

def test_word():
    with pytest.raises(ValueError):
        convert("1 ae to 2 PM")
    with pytest.raises(ValueError):
        convert("alaska AM to Ushuaia PM")
    with pytest.raises(ValueError):
        convert("1 AM to one PM")
    with pytest.raises(ValueError):
        convert("One PM to three PM")


def test_biggerhour():
    with pytest.raises(ValueError):
        convert("12 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("1:59 PM to 92:00 PM")
    with pytest.raises(ValueError):
        convert("92 PM to 3 AM")
    with pytest.raises(ValueError):
        convert("12 AM to 13 PM")

def test_biggerminute():
     with pytest.raises(ValueError):
        convert("1:60 AM to 3:33 PM")
     with pytest.raises(ValueError):
        convert("9 AM to 5:61 PM")
     with pytest.raises(ValueError):
        convert("9:99 AM to 5:00 PM")
     with pytest.raises(ValueError):
        convert("9:89 PM to 5:88 PM")

def test_jswrong():
     with pytest.raises(ValueError):
        convert("9 AP to 3 PM")
     with pytest.raises(ValueError):
        convert("9 to 3")
     with pytest.raises(ValueError):
        convert("AM TO PM")
     with pytest.raises(ValueError):
        convert("9 AM to 3 Pm")

def test_valid():
    assert convert("10:40 AM to 4:33 PM") == "10:40 to 16:33"
    assert convert("7 PM to 3 AM") == "19:00 to 03:00"
    assert convert("11:19 PM to 9 AM") == "23:19 to 09:00"

