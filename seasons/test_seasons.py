from seasons import conversion 
import pytest
import datetime 

yesterday = datetime.date.today() - datetime.timedelta(days=1)
yearago = datetime.date.today() - datetime.timedelta(days=365)
twoyears = datetime.date.today() - datetime.timedelta(days=730)

def test_yesterday():
    assert conversion(yesterday.isoformat()) == "One thousand, four hundred forty minutes"

def test_year():
    assert conversion(yearago.isoformat()) == "Five hundred twenty-five thousand, six hundred minutes"

def test_twoYears():
    assert conversion(twoyears.isoformat()) == "One million, fifty-one thousand, two hundred minutes"

def test_invalidSeparator():
    with pytest.raises(SystemExit):
        conversion("1990:01:01")

def test_invalidDate():
    with pytest.raises(SystemExit):
        conversion("2026-02-30")
