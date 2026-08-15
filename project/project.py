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
    x = input("Select an option ").strip().lower

    if x == "1":
        print("opening current currency value options...")
        time.sleep(1)
        clean_terminal()
        current_value_menu()

    else:
        print("please enter a valid option")

        #pauses the program for 2 seconds
        time.sleep(2)
        clean_terminal()
        main_menu()







def current_value_menu():
    ...




























if __name__ == "__main__":
    main()
