import sys
from fpdf import FPDF

class PDF(FPDF):

    def header(self):
        self.set_font("helvetica", style="B", size=15)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(20)
        self.image("shirtificate/shirtificate.png", x=20, y=70, w=170)



















def main():
    pdf = PDF()
    pdf.output("Test.pdf")



if __name__ == "__main__":
    main()
