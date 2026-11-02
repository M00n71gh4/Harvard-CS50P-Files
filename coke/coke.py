due = 50
done = False
#25, 10, 5

while done == False:

    #Dersom det enda er noe igjen å betale på brusen
    if due > 0:
        done = False
        print(f"Amount due: ", due)
        cash = input("Insert coin: ")
        cash = int(cash)

        #Maskinen aksepterer bare 25, 10 eller 5 cent
        if cash == 25 or cash == 10 or cash == 5:
            due = due - cash

    #Dersom maskinen gir tilbake veksel (*-1 for å gjøre negativt tall positivt)
    elif due <= 0:
        done = True
        print(f"Cash owed: ", due * -1)
        exit()



