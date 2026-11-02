import sys
import csv
from os.path import exists
from os import remove
from tabulate import tabulate

arg_lengt = len(sys.argv)

def rebuild_and_save(file_original, file_rebuild):

    #Åpner originalfilen
    with open(file_original) as file:
        #print("Ok")
        dreader = csv.DictReader(file)
        #print(tabulate(dreader, headers="firstrow", tablefmt="grid"))

        #Sletter filen slik at vi alltid begynner med en blank fil
        if exists(file_rebuild):
            remove(file_rebuild)


        with open(file_rebuild, "a") as new_file:
            writer = csv.DictWriter(new_file, ["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            #print(f"Writerow {file_rebuild}")


            for line in dreader:
                last_name, first_name = line["name"].split(", ")
                #print(f"first: {first_name} and {last_name}")
                writer.writerow({"first": first_name, "last": last_name, "house": line["house"]})

             # HER VAR JEG






match arg_lengt:
    case _ if arg_lengt < 3:
        sys.exit("Too few command-line arguments")
    case 3:
        if not exists(sys.argv[1]):
            sys.exit(f"Could not read {sys.argv[1]}")

        rebuild_and_save(sys.argv[1], sys.argv[2])

    case _:
        sys.exit("Too many command-line arguments")
