def main():

    resultado = get_fraction("Fraction: ")
    if resultado == 100:
        print("F")
    elif resultado == 0:
        print("E")
    else:
        print(f"{resultado}%")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            divis = x / y
            percentage = round(divis * 100)
            return percentage

        except (ValueError, ZeroDivisionError):
            pass


main()



































