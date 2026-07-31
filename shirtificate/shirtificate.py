import sys
from fpdf import FPDF

class PDF:
    pdf = FPDF()
    def __init__(self,name):
        name = input("What's your name?")
        if not name:
            sys.exit("Missing Name")
        self.name = name





