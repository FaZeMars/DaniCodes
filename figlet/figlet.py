import random
import sys
from pyfiglet import Figlet # type: ignore

figlet = Figlet()



def main():
    if sys.argv[1] == "0":
        x = input("Input: ")
        fo = figlet.getFonts()

        f = random.choice(fo)
        figlet.setFont(font=f)
        print(figlet.renderText(x))

    elif sys.argv[1] == "2"




main()
