
#str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

user_input = input("Input: ")
#omitt = ("A", "E", "I", "O", "U")

for c in user_input:
    #print(c.upper())
    if c.upper() == "A" or c.upper() == "E" or c.upper() == "I" or c.upper() == "O" or c.upper() == "U":
        user_input = user_input.replace(c, "")

print(user_input)