def main():

    resultado = get_fraction("Fraction: ")
    if resultado >= 99:
        print("F")
    elif resultado <= 1:
        print("E")
    else:
        print(f"{resultado}%")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if x > y:
                pass
            elif x < 0:
                pass
            else:
                divis = x / y
                percentage = round(divis * 100)
                return percentage

        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__"
    main()
