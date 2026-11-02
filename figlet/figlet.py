from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

args = sys.argv
#print(figlet.getFonts())




lenght_argument = len(args)

list_fonts = figlet.getFonts()
lenght_fonts = len(list_fonts)


#print(figlet.getFonts())


if lenght_argument == 3:
    if args[1] == "-f" or args[1] == "--font":

        if args[2] in list_fonts:
            tekst = input("Input: ")
            figlet.setFont(font=args[2])
            print(figlet.renderText(tekst))
        else:
            sys.exit(1)

    else:
        sys.exit(1)
elif lenght_argument == 1:
    tekst = input("Input: ")
    rand_num = random.randrange(0, lenght_fonts-1)
    figlet.setFont(font=list_fonts[rand_num])
    print(figlet.renderText(tekst))
else:
    sys.exit(1)


