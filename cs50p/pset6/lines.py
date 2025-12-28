import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith(".py") == False:
        sys.exit("Not a python file")

    with open(sys.argv[1]) as file:
        count = 0
        for row in file:
            line = row.lstrip()
            if line.startswith("#") or row.isspace():
                continue
            else:
                count += 1

    print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
