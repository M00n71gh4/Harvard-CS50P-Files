def main():
    userTime = input("What time is it?: ")
    totalTime = convert(userTime)

    # breakfast between 7:00 and 8:00
    # lunch between 12:00 and 13:00
    # and dinner between 18:00 and 19:00.

    if totalTime >= 7.00 and totalTime <= 8.00:
        print("breakfast time")
    elif totalTime >= 12.00 and totalTime <= 13.00:
        print("lunch time")
    elif totalTime >= 18.00 and totalTime <= 19.00:
        print("dinner time")

def convert(time):
    #Gets the time from the user
    userHour, userMinute = time.split(":")

    #Converts H and m from string to float
    userHour = float(userHour)
    userMinute = float(userMinute)

    userMinute = userMinute/60
    totalTime = userHour + userMinute

    return(totalTime)

if __name__ == "__main__":
    main()