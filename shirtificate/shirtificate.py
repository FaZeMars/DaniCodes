import sys
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__(orientation="P", unit="mm", format="A4")
        if not name:
            sys.exit("Input a name")
        self.name = name

    def header(self):
        self.set_font("helvetica", style="B", size=30)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(20)

        self.image("shirtificate.png", x=20, y=70, w=170)

        self.set_y(140)
        self.set_font("helvetica", style="B", size=15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{self.name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.add_page()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()



















def main():
    pdf = PDF()
    pdf.output("Test.pdf")



if __name__ == "__main__":
    main()
