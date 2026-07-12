import sys

command = sys.argv
if command[1].endswith(".py"):
    if len(command) == 2:
        try:
            with open(command[1]) as file:
                lineamount = 0
                for line in file:
                    if line.lstrip() == "" or line.startswith("#"):
                        lineamount += 0
                    else:
                        lineamount += 1
            print(lineamount)

        except FileNotFoundError:
            sys.exit("File does not exist")
            
    elif len(command) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

else:
    sys.exit("Not a Python file")
