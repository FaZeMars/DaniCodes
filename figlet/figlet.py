import random
import sys
from pyfiglet import Figlet # type: ignore

figlet = Figlet()



def main():
    if len(sys.argv) == 1:
        x = input("Input: ")
        fo = figlet.getFonts()
        f = random.choice(fo)
        figlet.setFont(font=f)
        print(figlet.renderText(x))

    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        fo = figlet.getFonts()

        if sys.argv[2] in fo:
            x = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(x))
        else:
            sys.exit("Invalid Usage")

    else:
         sys.exit("Invalid Usage")







main()
