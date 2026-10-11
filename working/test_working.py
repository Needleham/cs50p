
from working import convert
import pytest


def test_24hr():
    assert convert("2:00 PM to 9:00 PM") == "14:00 to 21:00"

def test_0s():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_halfhour():
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"

def test_nomin():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_12am():
    assert convert("12 AM to 12 PM") == "00:00 to 24:00"

def test_spacing():
    with pytest.raises(ValueError):
        convert("9AM to 6PM")

def test_overmins():
    with pytest.raises(ValueError):
        convert("9:60 AM to 4:60 PM")

def test_wrongtime():
    with pytest.raises(ValueError):
        convert("09 AM to 5:0001 PM")

def test_missingAM():
    with pytest.raises(ValueError):
        convert("09:00 to 05:00")

def test_noto():
    with pytest.raises(ValueError):
        convert("09:00 AM - 05:00 PM")
