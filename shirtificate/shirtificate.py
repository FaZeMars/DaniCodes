import sys
from fpdf import FPDF

class PDF(FPDF):

    def header(self, name):
        self.name = name

        self.set_font("helvetica", style="B", size=15)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(20)
        self.image("/workspaces/85688235/shirtificate/shirtificate.png", x=20, y=70, w=170)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{self.name} took CS50", align="c")



    @classmethod
    def get(cls):
        name = input("Name: ")
        if not name:
            sys.exit("Input a name")
        return cls(name)






def main():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()



















def main():
    pdf = PDF()
    pdf.output("Test.pdf")



if __name__ == "__main__":
    main()
