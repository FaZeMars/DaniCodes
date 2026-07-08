import random




def main():
    levelinput = get_level()

    correct = 0
    incorrect = 0
    while True:
        try:
            for problem in range(0,10):
                x = generate_integer(levelinput)
                y = generate_integer(levelinput)
                z = x + y
                intento = (input(f"{x} + {y}"))
                if intento == z:
                    correct += 1
                    break
                else:
                    print("EEE")
                    incorrect += 1
                    pass

        except ValueError:
            pass





def get_level():
    levelinput = int(input("Level: "))
    if int == 1 or int == 2 or int == 3:
        return levelinput

    else:
        raise ValueError


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        return x
    else:
        pass


if __name__ == "__main__":
    main()
