def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollah = str(d)
    dollah = dollah.replace("$", "")
    return(float(dollah))



def percent_to_float(p):
    perc = str(p)
    perc = perc.replace("%", "")
    return(float(perc)/100)

main()