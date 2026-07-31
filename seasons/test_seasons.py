import pytest
from datetime import date, timedelta
from seasons import Birth

def test_valid():
    oneyear = str(date.today() - timedelta(days=365))
    b = Birth(oneyear)
    assert b.convert() == "Five hundred twenty-five thousand, six hundred minutes"


