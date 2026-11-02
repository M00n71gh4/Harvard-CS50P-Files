try:
    my_list = {}

    while 1>0:
        item = input().upper()

        if item in my_list:
            count = my_list[item]
            my_list[item] = count + 1
        else:
            my_list[item] = 1


except:
    for items in sorted(my_list):
        print(f"{my_list[items]} {items}")
