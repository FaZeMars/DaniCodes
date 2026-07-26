from working import convert
import pytest

def test_word():
    with pytest.raises(ValueError):
            convert("1 ae to 2 PM")
            convert("alaska AM to Ushuaia PM")
            convert("1 AM to one PM")
            convert("One PM to three PM")

def test_biggerhour():
    with pytest.raises(ValueError):
         convert("12 AM to 13 PM")
         convert("1:59 PM to 92:00 PM")
         convert("92 PM to 3 AM")
         convert("12 AM to 13 PM")

def test_biggerminute():
     with pytest.raises(ValueError):
          convert("1:60 AM to 3:33 PM")
          convert("9 AM to 5:61 PM")
          convert("9:99 AM to 5:00 PM")
          convert("9:89 PM to 5:88 PM")

def test_jswrong():
     with pytest.raises(ValueError):
        convert("9 AP to 3 PM")
        convert("9 to 3")
        convert("AM TO PM")
        convert("9 AM to 3 Pm")

