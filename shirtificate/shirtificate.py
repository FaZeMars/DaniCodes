import sys
from fpdf2 import FPDF

class PDF:
    def __init__(self,name):
        name = input("What's your name?")
        if not name:
            sys.exit("Missing Name")
        self.name = name





