import random
import sys
from pyfiglet import Figlet # type: ignore

figlet = Figlet()



def main():
    if sys.argv[1] == 0:
        x = input("Input: ")
        fo = figlet.getFonts()
        for f in fo:
            



