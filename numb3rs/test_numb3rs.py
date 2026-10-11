from numb3rs import validate


def test_numb3rs():
    assert validate("127.255.255.10")
    assert validate("1.1.1.1")
    assert not validate("cat")
    assert not validate("1.1.1.1.1")
