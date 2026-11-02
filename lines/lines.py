from sys import argv


def main():

    arguments = argv
    lenght_arguments = len(arguments)

    if lenght_arguments < 2:
        exit("Too few command-line arguments")
    elif lenght_arguments > 2:
        exit("Too many command-line arguments")
    elif lenght_arguments == 2:
        file_exists(arguments[1])

def file_exists(file_name):
    file_name = str(file_name)
    count = 0

    if not "." in file_name:
        exit("Not a Python file")

    file, file_type = file_name.split(".")

    if not file_type == "py":
        exit("Not a Python file")

    with open(file_name, "r") as file:
        for line in file:
            count = count + check_line(line)

    print(count)


def check_line(code_line):

    code_line = str(code_line)

    code_line = code_line.strip()

    if code_line == "":
        return(0)
    if code_line.startswith("#"):
        return(0)

    return(1)




    open()
    print("Here is the code to count lines")



if __name__ == "__main__":
    main()

"""
Error messages:

    Too few command-line arguments
    Too many command-line arguments
    Not a Python file
File does not exist

"""