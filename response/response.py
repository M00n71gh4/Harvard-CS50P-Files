from validator_collection import validators, checkers, errors

def main():

    e_mail = input("What's your email address? ")
    try:
        validators.email(e_mail)
        print("Valid")
    except:
        print("Invalid")


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()