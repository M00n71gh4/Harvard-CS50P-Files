import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^([1][0-2]|[0-9])(?:\:)?([0-5][0-9])? ([APM]{2}) to ([1][0-2]|[0-9])(?:\:)?([0-5][0-9])? ([APM]{2})$", s)



    try:
        start_hour = match.group(1)
        start_minute = match.group(2)
        start_APM = match.group(3)
        end_hour = match.group(4)
        end_minute = match.group(5)
        end_APM = match.group(6)
    except:
        raise ValueError("Value out of range")

    if start_minute == None:
        start_minute = "00"

    if end_minute == None:
        end_minute = "00"

    return_value = hour_convert(start_hour, start_APM) + ":" + minute_write(start_minute) + " to " + hour_convert(end_hour, end_APM) + ":" + minute_write(end_minute)

    return(return_value)


def hour_convert(hour, APM):
    hour = int(hour)

    returnvalue = 0

    if APM == "AM":

        match hour:
            case 12:
                returnvalue = "00"
            case 11:
                returnvalue = str(hour)
            case 10:
                returnvalue = str(hour)
            case _ :
                returnvalue = "0" + str(hour)

    if APM == "PM":

        match hour:
            case 12:
                returnvalue = str(hour)
            case _ :
                returnvalue = str(hour + 12)

    return(returnvalue)

def minute_write(minutes):

    if int(minutes)>59:
        raise ValueError("Value out of range")

    return(minutes)

if __name__ == "__main__":
    main()