from bank import value

def main():
    test_start_with_hello()
    test_start_with_h()
    test_start_with_other()

def test_start_with_hello():
    assert value("hello")==0
    assert value("Hello")==0
    assert value("HELLO")==0
    assert value("Hello my friend")==0
    assert value("hello, how are you")==0

def test_start_with_h():
    assert value("holla")==20
    assert value("How do you do?")==20
    assert value("HOLLA")==20

def test_start_with_other():
    assert value("ay, holla")==100
    assert value("Good morning")==100
    assert value("APE")==100

#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername

if __name__ ==  "__main__":
    main()