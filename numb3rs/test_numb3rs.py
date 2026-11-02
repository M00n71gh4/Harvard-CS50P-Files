from numb3rs import validate

def main():
    test_validate_real_IP()
    test_validate_2long_IP()
    test_validate_2short_IP()
    test_validate_IP_with_char()
    test_validate_chk50()
#def test_validate2_simple():

    #assert validate2("0")=="Valid"
    #assert validate2("255")=="Valid"
    #assert validate2("35")=="Valid"
    #assert validate2("156")=="Valid"
    #assert validate2("256")=="Valid"


def test_validate_real_IP():
    assert validate("1.1.1.1")==True
    assert validate("127.0.0.1")==True
    assert validate("255.125.129.1")==True

def test_validate_2long_IP():
    assert validate("1.1.1.1.1")==False
    assert validate("127.0.0.1.54")==False
    assert validate("127.256.125.129.1")==False

def test_validate_2short_IP():
    assert validate("1.1.1")==False
    assert validate("127.1.54")==False
    assert validate("127.1")==False

def test_validate_IP_with_char():
    assert validate("1.B.1.1")==False
    assert validate("127.o.0.1")==False
    assert validate("127.256.125.1a9")==False

def test_validate_IP_out_of_range():
    assert validate("-1.1.1.1")==False
    assert validate("127.0.0.256")==False
    assert validate("256.125.129.1")==False

def test_validate_chk50():
    assert validate("256.255.255.255")==False
    assert validate("64.128.256.512")==False
    assert validate("8.8.8")==False
    assert validate("10.10.10.10.10")==False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334")==False
    assert validate("cat")==False



#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername

if __name__ ==  "__main__":
    main()