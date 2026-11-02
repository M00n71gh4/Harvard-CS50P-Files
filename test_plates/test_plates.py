    # start with at least two letters.”
    # X maximum of 6 characters (letters or numbers) X
    # X minimum of 2 characters.” X
    # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # X The first number used cannot be a ‘0’.”
    # X No periods, spaces, or punctuation marks are allowed.”

from plates import is_valid

def main():
    test_is_valid_Amount_Characters()
    test_is_valid_Number_place()
    test_is_first_number()
    test_is_punctution()
    test_is_Start_Alpha()

def test_is_Start_Alpha():
    #Write test codet
    assert is_valid("6R")==False
    assert is_valid("G9")==False
    assert is_valid("69")==False
    assert is_valid("GR")==True

def test_is_valid_Amount_Characters():
    #Write test codet
    assert is_valid("IAMGREAT")==False
    assert is_valid("I")==False
    assert is_valid("IAM")==True

def test_is_valid_Number_place():
    #Write test codet
    assert is_valid("GRE4T")==False
    assert is_valid("GREA4")==True

def test_is_first_number():
    #Write test codet
    assert is_valid("GRE04")==False
    assert is_valid("GRE44")==True

def test_is_punctution():
    #Write test codet
    assert is_valid("GRE 4")==False
    assert is_valid("GRE,4")==False
    assert is_valid("GRE.4")==False
    assert is_valid("GRE44")==True




#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername

if __name__ ==  "__main__":
    main()