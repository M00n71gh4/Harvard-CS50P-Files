from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_Errors()

#convert expects a str and returns that fraction as a percentage rounded to the nearest int
def test_convert():
    assert convert("0/100")==0
    assert convert("99/100")==99
    assert convert("50/100")==50

#gauge expects an int and returns a str that is:
def test_gauge():
    assert gauge(0)=="E"
    assert gauge(100)=="F"
    assert gauge(50)=="50%"
    assert gauge(99)=="F"
    assert gauge(1)=="E"


def test_Errors():
    with pytest.raises(ValueError):
        convert("B/f")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


if __name__ ==  "__main__":
    main()

#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername