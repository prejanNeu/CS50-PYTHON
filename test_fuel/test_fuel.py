from fuel import convert, gauge
import pytest

def test_input():
    assert convert("1/2")==50
    assert convert("4/5")==80
    assert convert("0/100")==0

def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    with pytest.raises(ValueError):
        convert("3/2")

def test_output():
    assert gauge(1)=="E"
    assert gauge(100)=="F"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"
    assert gauge(33)=="33%"



