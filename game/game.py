import random
import sys

def main():

    while True:
        lev = int(input("Level: "))
        if 0 < lev:
            break
        else:
            pass

    numbertoguess = random.randint(1, lev)

    while True:
        try:
            guess = int(input("Guess: "))
            if numbertoguess == guess:
                print("Just right!")
                sys.exit()
            elif 0 < guess < numbertoguess:
                print("Too small!")
                pass
            elif 0 < numbertoguess < guess:
                print("Too large!")
            else:
                pass

        except EOFError:
            sys.exit()

        except ValueError:
            pass


main()
