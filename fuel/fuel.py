def main():

    inp = input("Fraction: ")


    print(w)

    while True:
        try:
            x, y = inp.split("/")
            num1 = int(x)
            num2 = int(y)
            w = x + y
            return int(w)

        except ValueError:
            pass


main()



































