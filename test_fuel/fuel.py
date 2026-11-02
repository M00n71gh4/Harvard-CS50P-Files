def main():
    try:
        repeat = True

        while repeat == True:
            user_input = input("Fraction: ")

            if "/" in user_input:
                converted = convert(user_input)
                print(gauge(converted))
                repeat = False

    except (ValueError, ZeroDivisionError):
        raise
#convert expects a str and returns that fraction as a percentage rounded to the nearest int
def convert(fraction):
    x, y = fraction.split("/")

    result = (float(x)/float(y))*100.0
    return(int(round(result)))

#gauge expects an int and returns a str that is: E F Z
def gauge(percentage):
    returnvalue = ""
    percentage = int(percentage)

    if percentage <= 1:
        returnvalue = "E"
    elif percentage >= 99:
        returnvalue = "F"
    else:
        returnvalue = f"{percentage}%"

    return(returnvalue)


if __name__ == "__main__":
    main()

"""
def main_function():
    repeat = True

    while repeat == True:
        user_input = input("Fraction: ")

        if "/" in user_input:
            x, y = user_input.split("/")

            if int(x) <= int(y) and x.isdigit() and y.isdigit():

                result = (float(x)/float(y))*100.0
#GAUGE
                if result <= 1:
                    print("E")
                elif result >= 99:
                    print("F")
                else:
                    print(f"{int(round(result))}%")

                repeat = False


try:

    main_function()


except (ValueError, ZeroDivisionError):
    main_function(  )
"""