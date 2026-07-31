import sys
from fpdf import FPDF

class PDF(FPDF):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    def header(self):
        self.set_font("helvetica", style="B", size=15)



