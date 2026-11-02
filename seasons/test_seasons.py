from seasons import date_caclulations

format = "%Y-%m-%d"

def test_valid_date():
    date_calc = date_caclulations("1978-09-22", format)
    date_calc.ceck = True

def test_invalid_valid_date():
    date_calc = date_caclulations("22-09-1978", format)
    date_calc.ceck = False



if __name__ ==  "__main__":
    main()
