from working import convert
import pytest

def main():
    test_convert_AM_long()
    test_convert_PM_long()
    test_convert_AM_PM_long()
    test_convert_PM_AM_long()
    test_convert_AM_short()
    test_convert_PM_short()
    test_convert_AM_PM_short()
    test_convert_PM_AM_short()
    test_convert_PM_AM_Mix_w_minutes()

def test_convert_AM_long():
    assert convert("1:00 AM to 5:00 AM")=="01:00 to 05:00"
    assert convert("3:00 AM to 5:00 AM")=="03:00 to 05:00"
    assert convert("10:00 AM to 11:00 AM")=="10:00 to 11:00"
    assert convert("12:00 AM to 3:00 AM")=="00:00 to 03:00"

def test_convert_PM_long():
    assert convert("12:00 PM to 5:00 PM")=="12:00 to 17:00"
    assert convert("2:00 PM to 5:00 PM")=="14:00 to 17:00"
    assert convert("9:00 PM to 11:00 PM")=="21:00 to 23:00"
    assert convert("6:00 PM to 7:00 PM")=="18:00 to 19:00"

def test_convert_AM_PM_long():
    assert convert("12:00 AM to 7:00 PM")=="00:00 to 19:00"
    assert convert("3:00 AM to 8:00 PM")=="03:00 to 20:00"
    assert convert("12:00 AM to 12:00 PM")=="00:00 to 12:00"
    assert convert("6:00 AM to 7:00 PM")=="06:00 to 19:00"

def test_convert_PM_AM_long():
    assert convert("6:00 PM to 12:00 AM")=="18:00 to 00:00"
    assert convert("12:00 PM to 11:00 AM")=="12:00 to 11:00"
    assert convert("9:00 PM to 10:00 AM")=="21:00 to 10:00"
    assert convert("10:00 PM to 3:00 AM")=="22:00 to 03:00"


def test_convert_AM_short():
    assert convert("1 AM to 5 AM")=="01:00 to 05:00"
    assert convert("3 AM to 5 AM")=="03:00 to 05:00"
    assert convert("10 AM to 11 AM")=="10:00 to 11:00"
    assert convert("12 AM to 3 AM")=="00:00 to 03:00"

def test_convert_PM_short():
    assert convert("12 PM to 5 PM")=="12:00 to 17:00"
    assert convert("2 PM to 5 PM")=="14:00 to 17:00"
    assert convert("9 PM to 11 PM")=="21:00 to 23:00"
    assert convert("6 PM to 7 PM")=="18:00 to 19:00"

def test_convert_AM_PM_short():
    assert convert("12 AM to 7 PM")=="00:00 to 19:00"
    assert convert("3 AM to 8 PM")=="03:00 to 20:00"
    assert convert("12 AM to 12 PM")=="00:00 to 12:00"
    assert convert("6 AM to 7 PM")=="06:00 to 19:00"

def test_convert_PM_AM_short():
    assert convert("6 PM to 12 AM")=="18:00 to 00:00"
    assert convert("12 PM to 11 AM")=="12:00 to 11:00"
    assert convert("9 PM to 10 AM")=="21:00 to 10:00"
    assert convert("10 PM to 3 AM")=="22:00 to 03:00"

def test_convert_PM_AM_Mix_w_minutes():
    #PM-AM
    assert convert("6:59 PM to 12:23 AM")=="18:59 to 00:23"
    assert convert("12:00 PM to 11:03 AM")=="12:00 to 11:03"
    #AM-PM
    assert convert("12:10 AM to 12:43 PM")=="00:10 to 12:43"
    assert convert("6:48 AM to 7:59 PM")=="06:48 to 19:59"

def test_convert_Error():
    with pytest.raises(ValueError):
        convert("6:48 AM to 7:60 PM")

    with pytest.raises(ValueError):
        convert("6:48 AM 7:60 PM")
    #6:48 AM to 7:60 PM






#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername

if __name__ ==  "__main__":
    main()


    #Runs with pytest filename.py