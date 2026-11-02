input_list = ["Adieu, adieu, to"]

try:
    loop = True
    while loop == True:
        input_list.append(input("Name: "))
except EOFError:
    #print(f"{input_list[0]}", end = " ")
    list_lenght = len(input_list)
    #print(list_lenght)
    print(f"\n{input_list[0]}", end = " ")

    if list_lenght == 3:
        #print(f"{input_list[1]} and {input_list[2]}", end=", ")
        print(f"{input_list[1]} and", end=" ")
    elif list_lenght > 3:
        i = 1
        while i < list_lenght - 1:
            print(f"{input_list[i]}", end=", ")
            i += 1
        print("and", end = " ")

    print(f"{input_list[-1]}")





