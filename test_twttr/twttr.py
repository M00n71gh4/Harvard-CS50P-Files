def main():
    word_to_shorten =input()
    shorten(word_to_shorten)


def shorten(word):
    #str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

    user_input = word
    #omitt = ("A", "E", "I", "O", "U")

    for c in user_input:
        #print(c.upper())
        if c.upper() == "A" or c.upper() == "E" or c.upper() == "I" or c.upper() == "O" or c.upper() == "U":
            user_input = user_input.replace(c, "")

    return(user_input)


if __name__ == "__main__":
    main()


