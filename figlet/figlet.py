import random
import sys
from pyfiglet import Figlet # type: ignore

figlet = Figlet()



def main():
    if sys.argv[1] == "0":
        x = input("Input: ")
        fo = figlet.getFonts()
        for fonti in fo:
            f = random.choice("fonti")
        figlet.setFont(font=f)
        print(figlet.renderText(x))




main()
