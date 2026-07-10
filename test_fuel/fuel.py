def main():

    resultado = convert(input("Fraction: "))
    if resultado >= 99:
        print("F")
    elif resultado <= 1:
        print("E")
    else:
        print(f"{resultado}%")


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        elif x < 0:
            raise ValueError
        else:
            divis = x / y
            percentage = round(divis * 100)
            return percentage

    except (ValueError, ZeroDivisionError):
        raise ValueError


if __name__ == "__main__":
    main()
