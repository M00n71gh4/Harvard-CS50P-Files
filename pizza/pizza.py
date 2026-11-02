import sys
import csv
from os.path import exists
from tabulate import tabulate

arg_lenght = len(sys.argv)

def check_existence(file_name):

    if not exists(file_name):
        sys.exit("File does not exist")

    if not file_name[-4:] == ".csv":
        sys.exit("Not a CSV file")


    pizzas = []
    with open(file_name) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))

match arg_lenght:
    case 1:
        sys.exit("Too few command-line arguments")
    case 2:
        check_existence(sys.argv[1])
    case _:
        sys.exit("Too many command-line arguments")
