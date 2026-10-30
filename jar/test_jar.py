from jar import Jar 
import pytest

def test_init():
    jar = Jar(5)
    assert  jar.capacity == 5
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(1)
    assert jar.size == 1 
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(20)

