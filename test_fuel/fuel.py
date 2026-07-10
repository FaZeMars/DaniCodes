def main():

    resultado = convert(input("Fraction: "))
    printed = gauge(resultado)
    print(printed)


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
            percent = round(divis * 100)
            return percent

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")



if __name__ == "__main__":
    main()
