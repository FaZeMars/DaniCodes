import sys

command = sys.argv
if command[0].endswith(".py"):
    try:
        with open command[1] as file:
            lineamount = 0
            for line in file:
                if line.startswith("#"):
                    lineamount += 0
                elif line.startswith('"""'):
                    lineamount += 0
                elif line.startswith





    except FileNotFoundError:
        sys.exit("File does not exist")

else:
    sys.exit("Not a Python file")
