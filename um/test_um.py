from um import count
import pytest

def test_um():
    assert count("um") == 1

def test_ummark():
    assert count("um?") == 1

def test_sentence():
    assert count("um, thanks for the album") == 1

def test_multiple():
    assert count("um, how, um, are you?") == 2

def test_capitals():
    assert count("UM, I want to Um test") == 2

def test_fullstops():
    assert count("Um, thanks um.....") == 2
    

