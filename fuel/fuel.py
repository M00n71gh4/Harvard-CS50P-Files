def main_function():
    repeat = True

    while repeat == True:
        user_input = input("Fraction: ")

        if "/" in user_input:
            x, y = user_input.split("/")

            if int(x) <= int(y) and x.isdigit() and y.isdigit():

                result = (float(x)/float(y))*100.0

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
