
month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#1963-09-08 <-  September 8, 1936
#               9/8/1636
def check_date():
    split_date = ""
    month_number = ""

    input_date = input("Date: ")
    if "," in input_date:
        input_date = input_date.replace(",", "")
        split_date = input_date.split()
        month_number = month_list.index(split_date[0])+1
    elif "/" in input_date:
        split_date = input_date.split("/")
        month_number = split_date[0]

    day = f"{int(split_date[1]):02}"
    month = f"{int(month_number):02}"
    year = f"{int(split_date[2])}"

    if int(day) <= 31 and int(month) <= 12:
        print(f"{year}-{month}-{day}")
        return True
    else:
        return False

try:
    end_checking = False
    while end_checking == False:
        end_checking = check_date()

except:
    check_date()