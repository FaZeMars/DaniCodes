import random
import sys

def main():
    levelinput = get_level()
    correct = 0
    try:
        for problem in range(0,10):
            x = generate_integer(levelinput)
            y = generate_integer(levelinput)
            z = x + y
            incorrect = 0
            while True:
                intento = int(input(f"{x} + {y} ="))
                if intento == z:
                    correct += 1
                    break

                else:
                    print("EEE")
                    incorrect += 1
                    if incorrect == 3:
                        incorrect = 0
                        print(f"{x} + {y} = {z}")
                        break

        print(f"Score: {correct}")


    except ValueError:
        pass
    except EOFError:
        sys.exit(" Program Closed")




def get_level():
    while True:
        try:
            levelinput = int(input("Level: "))
            if levelinput == 1 or levelinput == 2 or levelinput == 3:
                return levelinput

        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        return x
    elif level == 2:
        x = random.randint(10, 99)
        return x
    elif level == 3:
        x = random.randint(100, 999)
        return x
    else:
        pass


if __name__ == "__main__":
    main()
