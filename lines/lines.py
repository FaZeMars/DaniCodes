import sys

command = sys.argv
if command[0].endswith(".py"):
    try:
        with open command[1] as file:
            

    except FileNotFoundError:
        sys.exit("File does not exist")

else:
    sys.exit("Not a Python file")
