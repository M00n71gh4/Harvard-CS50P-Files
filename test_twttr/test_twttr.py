from twttr import shorten

def test_shorten_small():
    assert shorten("twitter")== "twttr"

def test_shorten_large():
    assert shorten("TWITTER")== "TWTTR"

def test_shorten_mixed():
    assert shorten("TwItTeR")== "TwtTR"

def test_shorten_number():
    assert shorten("12578") == "12578"

def test_shorten_Punct():
    assert shorten("?,!.") == "?,!."