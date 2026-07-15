import sys
import os

def main():
    pass



def validate():
    command = sys.argv.lowercase()
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        valid_Extensions = ["jpeg", "jpg", "png"]
        root1, ext1 = os.path.splitext(command[1])
        root2, ext2 = os.path.splitext(command[2])

        if ext1 == ext2:
            if ext1 in valid_Extensions and ext2 in valid_Extensions:
                return command[1] and command[2]
            else:
                sys.exit(")

        else:
            sys.exit("Input and Output have different extensions")







if __name__ == "__main__":
    main()
