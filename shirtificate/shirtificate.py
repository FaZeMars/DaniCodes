from fpdf2 import FPDF

class Shirt:
    def __init__(self, name):
        self.name = name



    @classmethod
    def get(cls):
        name = input("What's your name?")
        return cls(name)
