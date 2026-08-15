# BlueApp

import sys
import re
import time
import os




def main():
    main_menu()






def main_menu():
    #Opens up a main menu section for the user to select what they want to do, then calls the function the user wants to use
    menu = ["1)Current Value",
            "2)Conversion"
            ]
    print(*menu, sep="\n")
    x = input("Select an option ").strip().lower

    if x == "test":
        print("please enter a valid option")
        main_menu()

    else:
        ...



























if __name__ == "__main__":
    main()
