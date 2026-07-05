import random
import sys
from pyfiglet import Figlet # type: ignore

figlet = Figlet()



def main():
    if sys.argv[1] == "0":
        x = input("Input: ")
        fo = figlet.getFonts()
        random.choice(figlet.setFont(font=fo))
        print(figlet.renderText(x))




main()
