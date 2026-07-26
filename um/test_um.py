from um import count

def test_valid():
    assert count("hello, um, world, um, how are you?") == 2
    assert count("Mr. president, um, what are you doing?") == 1

def test_uminword():
    assert count("yummy") == 0
def test_uppercase():
    assert count("UM, um, Um, um") == 4
