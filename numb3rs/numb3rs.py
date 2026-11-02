import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
"""
def validate(ip):
    ip = str(ip)
    range1, range2, range3, range4 = ip.split(".")
    range1 = int(range1)
    range2 = int(range2)
    range3 = int(range3)
    range4 = int(range4)

    error_message = "False"
    status = "True"

    if  range1 <= 255 and  range1 >= 0:
        pass
    else:
        sys.exit(error_message)
    if range2 <= 255 and range2 >= 0:
        pass
    else:
        sys.exit(error_message)
    if range3 <= 255 and range3 >= 0:
        pass
    else:
        sys.exit(error_message)
    if range4 <= 255 and range4 >= 0:
        pass
    else:
        sys.exit(error_message)

    return("True")
"""
def validate(ip):
    ip = str(ip)

    if re.search(r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.{1}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.{1}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.{1}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", ip):
        return(True)
    else:
        return(False)



if __name__ == "__main__":
    main()