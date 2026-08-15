# BlueApp

import sys
import re
import time
import os
import json
import requests

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    main_menu()








def main_menu():
    #Opens up a main menu section for the user to select what they want to do, then calls the function the user wants to use
    menu = ["1)Current Value",
            "2)Conversion"
            ]
    print(*menu, sep="\n")
    x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()

    try:
        if x == "1":
            print("Opening current currency value options...")
            time.sleep(1)
            clean_terminal()
            current_value_menu()

        elif x == "2":
            print("Opening current currency conversion options...")
            time.sleep(1)
            clean_terminal()
            currency_conversion_menu()


        else:
            print("please enter a valid option")

            #pauses the program for 1 second, then goes back to the main menu
            time.sleep(1)
            clean_terminal()
            main_menu()

    except (EOFError, KeyboardInterrupt):
        sys.exit("Closing the program...")







def current_value_menu():
    #Opens up a menu including the options for quoting specific currency types, then, according to the user input, calls a function which returns the current value of this currency type
    menu = ["1)Dólar Oficial",
            "2)Dólar Blue",
            "3)Dólar MEP / Bolsa",
            "4)Dólar Tarjeta",
            "5)Dólar Cripto",
            "6)Other currencies:",
            "7)Main Menu"
    ]

    print(*menu, sep="\n")

    x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()

    if x == "1":
        get_dollar("oficial")
    elif x == "2":
        get_dollar("blue")
    elif x == "3":
        get_dollar("bolsa")
    elif x == "4":
        get_dollar("tarjeta")
    elif x == "5":
        get_dollar("cripto")

    elif x == "6":
        get_other_currency()

    elif x == "7":
        print("Returning to main menu...")
        time.sleep(1.5)
        clean_terminal()
        main_menu()

    else:
        print("Please input a valid option.")
        time.sleep(1)
        clean_terminal
        current_value_menu()





def currency_conversion_menu():
    ...


def get_other_currency():
    ...





##############################################################################################
def get_dollar(type):
    
    typelist = ["oficial", "blue", "bolsa", "tarjeta", "cripto"]

    if type in typelist:
        url = f"https://dolarapi.com/v1/dolares/{type}"
        pre_type = requests.get(url)
        try:
            # o = variable used to store the requests.get json
            o = pre_type.json()
            type_buy = o["compra"]
            type_sell = o["venta"]
            timeupdate = o["fechaActualizacion"]

            print(f"Sale Value: {type_sell}",
                  f"Purchase Value: {type_buy}",
                  f"Last updated: {timeupdate}",
                  sep="\n"
                  )
            while True:
                answer = input("Do you wish to do something else? (y/n) ").strip().lower()
                if answer == "y":
                    print("Going back to the main menu...")
                    time.sleep(1)
                    clean_terminal()
                    main_menu()
                elif answer == "n":
                    clean_terminal()
                    sys.exit("Closing the program...")
                else:
                    clean_terminal()
                    print("")
        except requests.RequestError:
            sys.exit("Connection Error")
















if __name__ == "__main__":
    main()
