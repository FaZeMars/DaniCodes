import sys
import os
from PIL import Image, ImageOps

def main():
    before, after = validate()
    student_resized = refit(before)
    studentclean = paste(student_resized, after)



def validate():
    command = sys.argv
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        valid_Extensions = [".jpeg", ".jpg", ".png"]
        root1, ext1 = os.path.splitext(command[1]).lower
        root2, ext2 = os.path.splitext(command[2]).lower

        if ext1 == ext2:
            if ext1 in valid_Extensions and ext2 in valid_Extensions:
                return command[1], command[2]
            else:
                sys.exit("Not a valid extension")

        else:
            sys.exit("Input and Output have different extensions")

def refit(s):
    student_image = Image.open(s)
    templateimage = Image.open("shirt.png")
    student_resized = ImageOps.fit(student_image, "shirt.png")
    return student_resized

def paste(s, y):
    readystudent = refit(s)
    shirtemplate = Image.open("shirt.png")
    readystudent.paste(shirtemplate, shirtemplate)
    readystudent.save(y)
# y being sys.argv[1]







if __name__ == "__main__":
    main()
