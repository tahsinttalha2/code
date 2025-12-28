import sys
import csv
import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith(".csv") == False:
        sys.exit("Not a python file")

    list = []

    with open(sys.argv[1]) as file:
        lines = csv.reader(file)
        headers = next(lines)

        for line in lines:
            list.append(line)

        print(tabulate.tabulate(list, headers=headers, tablefmt = "grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
