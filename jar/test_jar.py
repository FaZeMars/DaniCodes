import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


    with pytest.raises(ValueError):
        Jar(-4)

    with pytest.raises(ValueError):
        Jar("cat")



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    assert jar.capacity == 12

    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3
    assert jar.capacity == 10

    jar = Jar(3)

    with pytest.raises(ValueError):
        jar.deposit(-3)

    with pytest.raises(ValueError):
        jar.deposit("cat")

    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar(9)
    jar.deposit(7)
    jar.withdraw(4)

    assert jar.capacity == 9
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(8)

    with pytest.raises(ValueError):
        jar.withdraw(-4)

    with pytest.raises(ValueError):
        jar.withdraw("cat")
