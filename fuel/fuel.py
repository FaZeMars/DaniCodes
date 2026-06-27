def main():

    inp = input("Fraction: ")



def get_int(inp):
    while True:
        try:
            input(inp)
            x, y = inp.split("/")
            num1 = int(x)
            num2 = int(y)
            w = num1 + num2
            return w

        except ValueError:
            pass

        print(w)


main()



































