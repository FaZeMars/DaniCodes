# BlueApp

import sys
import re
import time
import os




def main():
    main_menu()

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')






def main_menu():
    #Opens up a main menu section for the user to select what they want to do, then calls the function the user wants to use
    menu = ["1)Current Value",
            "2)Conversion"
            ]
    print(*menu, sep="\n")
    x = input("Select an option (e.g.: 1, 2 ...) ", end="\n").strip().lower()

    try:
        if x == "1":
            print("Opening current currency value options...")
            time.sleep(1)
            clean_terminal()
            current_value_menu()

        elif x == "2":
            ...

        else:
            print("please enter a valid option")

            #pauses the program for 2 seconds
            time.sleep(2)
            clean_terminal()
            main_menu()


    except (EOFError, KeyboardInterrupt):
        sys.exit("Closing the program...")







def current_value_menu():
    #Opens up a menu including the options for quoting specific currency types, then, according to the user input, calls a function which returns the current value of this currency type
    menu = ["1)Dólar Blue",
            "2)Dólar Mep

    ]





























if __name__ == "__main__":
    main()
