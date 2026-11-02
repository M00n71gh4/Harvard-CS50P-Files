from um import count

def main():
    test_count()

def test_count():
    #Write test codet
    assert count("Rhis is um, good um stuff")==2

def test_count_na():
    assert count("Rhis is yummy")==0

def test_count_mix():
    assert count("Rhis is um, yummy um stuff")==2

def test_count_Special_char():
    assert count("Um... what are regular expressions?")==1
    assert count("Um, thanks, um, regular expressions make sense now.")== 2

#if testet from a folder, it also requires __init__.py (Tells Python to create the folder as a package) -> pytest foldername

if __name__ ==  "__main__":
    main()


    #Runs with pytest filename.py