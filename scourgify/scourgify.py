import sys

def main():
    pass



def validate():
    command = sys.argv.lowercase()
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if command[1].endswith(".") and command[2].endswith(".csv"):
            return command[1], command[2]

        else:
            sys.exit("Not a CSV file")





if __name__ == "__main__":
    main()
