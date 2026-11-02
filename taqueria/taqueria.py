menu_list = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

try:
    total_value = 0
    while 1 > 0:
        item = input("Item: ").title()

        if item in menu_list:
            value = menu_list[item]
            total_value = total_value + value
            print(f"Total: ${total_value:.2f}")

except EOFError:
    print("")



