def main():
    fraction = get_fuel("Fraction: ")
    twovalues = fraction.split("/")

    


def get_fuel(prompt):
    while True:
        try:
            return int(input(prompt))
        except (ValueError, ZeroDivisionError):
            pass





main()























