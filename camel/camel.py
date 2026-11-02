var = input("camelCase: ")


for c in var:
    #print(c)
    if c == c.upper():
        var = var.replace(c, "_" + c.lower())

print("snake_case: " + var)
