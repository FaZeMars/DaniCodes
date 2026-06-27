def main():

resultado = get_fraction("Fraction: ")


def get_fraction(prompt):
    while True:
        try:
            x, y = int(input(prompt).split("/"))
            divis = x / y

        except (ValueError, ZeroDivisionError):
            pass






































