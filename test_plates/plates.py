    #“All vanity plates must start with at least two letters.”
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    #“No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    s = str(s)
    if correct_lenght(s):
        if check_digits(s) and special_char(s):
            return(True)
        else:
            return(False)
    else:
        return(False)


def special_char(s):
    s = str(s)
    if "." in s or "," in s or " " in s:
        return(False)
    else:
        return(True)

def start_two_letters(s):
    s = str(s)

    if s[0].isalpha() and s[1].isalpha():
        return(True)
    else:
        return(False)


def correct_lenght(s):
    s = str(s)
    plate_lenght = len(s)

    if plate_lenght >= 2 and plate_lenght <= 6:
        return(True)
    else:
        return(False)

def check_digits(s):
    s = str(s)

    if start_two_letters(s):
        found_digit = False
        i = 0
        if any(ch.isdigit() for ch in s):
            for ch in s:
                if ch.isnumeric():
                    if int(ch) > 0 and found_digit == False:
                        last_part = s[i:]
                        if last_part.isnumeric():
                            return(True)
                        else:
                            return(False)
                        found_digit = True
                    else:
                        return(False)
                i = i+1
        else:
            return(True)#VAr True





if __name__ == "__main__":
    main()

