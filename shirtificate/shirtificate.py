import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate/shirtificate.png", 0, 0, 0)
        self.set_font("helvetica", style="B", size=15)



