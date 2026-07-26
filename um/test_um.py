from um import count

def test_valid():
    assert count("hello, um, world, um, how are you?") == 2
    assert count("Mr. president, um, why are)
