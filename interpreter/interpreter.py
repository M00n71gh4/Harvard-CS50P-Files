userInput = input("Expression: ")
x, y, z = userInput.split(" ")

x = float(x)
z = float(z)

match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "/":
        print(x/z)
    case _:
        print("What?")