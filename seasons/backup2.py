from datetime import date, datetime, timedelta
import inflect # Flertalls ord
import sys
date_format = "%Y-%m-%d" # %H:%M:%S"
def main():

    date_of_birth = input("Date of birth: ")
    #date_of_birth = f"{date_of_birth} 00:00:00"
    date_of_birth = check(date_of_birth, date_format)

    date_diff = calculate(date_of_birth)

    date_diff = date_diff.days/24/60

    print(convert(date_diff))



def check(date_to_check, format): #Checks for right forma and returns datetime object with time = 00:00:00
    try:
        return datetime.strptime(date_to_check, format)
    except ValueError:
        sys.exit("Invalid date")

def calculate(birth_date):

    str_date_now = datetime.strptime(datetime.today(), date_format) #datetime.today()
    str_date_now = str_date_now.replace(hour=0, minute=0, second=0, microsecond=0)

    time_diff = str_date_now - birth_date

    return time_diff

def convert(date_diff):

    inf = inflect.engine()

    return inf.number_to_words(date_diff, andword="").capitalize()



if __name__ == "__main__":
    main()






#date_of_birth = f"{birth}"

#date_now = datetime.strptime(str_date_now, date_format)

"""
time_delta = str_date_now - date_of_birth
#print(str_date_now)
print(date_of_birth)
print(str_date_now)
print(time_delta)
time_delta = int(datetime.strftime(time_delta))
print(time_delta.total_seconds()/60)
"""
