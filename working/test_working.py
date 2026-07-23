from working import convert

def test_word():
    assert convert("1 ae to 2 PM") == ValueError
    assert convert("1 AM to one PM") == ValueError
    assert convert("One PM to three PM") == ValueError
    assert convert("alaska AM to Ushuaia PM") == ValueError


