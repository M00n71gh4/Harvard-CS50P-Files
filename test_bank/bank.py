def main():

    strGreeting = input("Greeting: ")
    value(strGreeting)


def value(greeting):
    greeting = greeting.strip()
    greeting = greeting[:5]
    greeting = greeting.capitalize()


    if greeting == "Hello":
        return("$0")
    elif greeting[0] == "H":
        return("$20")
    else:
        return("$100")


if __name__ == "__main__":
    main()









