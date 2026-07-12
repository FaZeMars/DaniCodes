import sys

command = sys.argv


if len(command) == 1:
    sys.exit("Too few command-line arguments")
elif len(command) > 2:
    sys.exit("Too many command-line arguments")
else:
    try:
        if command[1].endswith(".csv"):


            if command[1] == "sicilian.csv":
                with open("sicilian.csv") as file:
                    for line in file:
                        print

            elif command[1] == "regular.csv":
                with open("regular.csv") as file:
                    for line in file:
                        print

            else:
                raise FileNotFoundError

        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File not found")







