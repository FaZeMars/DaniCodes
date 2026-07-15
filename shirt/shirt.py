import sys

def main():
    pass



def validate():
    command = sys.argv.lowercase()
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
            sys.exit("Not a CSV file")





if __name__ == "__main__":
    main()
