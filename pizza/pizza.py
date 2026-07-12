import sys

command = sys.argv


if len(command) == 1:
    sys.exit("Too few command-line arguments")
elif len(command) > 2:
    sys.exit("Too many command-line arguments")
else:
    if command[1].endswith(".csv"):
        if command[1] == "sicilian.csv":
            with open("sicilian.csv") as file:
        elif command[1] == "regular.csv":
            with open("regular.csv") as file:
        else:
            raise FileNotFoundError(")
    else:
        sys.exit("Not a CSV file")







