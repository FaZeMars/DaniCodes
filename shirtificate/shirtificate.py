import sys
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=15)
        self.image("shirtificate/shirtificate.png", 0, 0, 0)
        self.cell(10, 0,)
















def main():
    ...


if __name__ == "__main__":
    main()
