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
    try:
        main_menu()
    except (EOFError, KeyboardInterrupt):
        sys.exit("Closing the program...")


def main_menu():
    #Opens up a main menu section for the user to select what they want to do, then calls the function the user wants to use
    menu = ["1)Current Value",
            "2)Conversion"
            ]
    print(*menu, sep="\n")
    x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()

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
        clean_terminal()
        main_menu()










"""Current Value Options""" ##########################################################
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
        get_dollar("dolares/oficial")
    elif x == "2":
        get_dollar("dolares/blue")
    elif x == "3":
        get_dollar("dolares/bolsa")
    elif x == "4":
        get_dollar("dolares/tarjeta")
    elif x == "5":
        get_dollar("dolares/cripto")

    elif x == "6":
        clean_terminal()
        get_other_currency()

    elif x == "7":
        print("Returning to main menu...")
        time.sleep(1.5)
        clean_terminal()
        main_menu()

    else:
        print("Please input a valid option.")
        time.sleep(0.5)
        clean_terminal
        current_value_menu()




def get_dollar(type):

    type = type.strip().lower()

    #type of currencies available
    type_list = ["dolares/oficial",
                 "dolares/blue",
                 "dolares/bolsa",
                 "dolares/tarjeta",
                 "dolares/cripto",
                 "cotizaciones/clp",
                 "cotizaciones/eur",
                 "cotizaciones/brl",
                 "cotizaciones/uyu"
                 ]

    if type in type_list:
        try:
            url = f"https://dolarapi.com/v1/{type}"
            pre_type = requests.get(url)
            # o = variable used to store the requests.get json
            o = pre_type.json()
            type_buy = o["compra"]
            type_sell = o["venta"]
            coin_name = o["nombre"]
            coin = o["moneda"]
            timeupdate = o["fechaActualizacion"]


            re = re.matches(r"^(\d{4})-)





            clean_terminal()
            print(f"{coin} {coin_name}",
                  f"Sale Value: {type_sell}",
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
        except requests.RequestException:
            sys.exit("Connection Error")



def get_other_currency():
    menu = ["1)Euro",
            "2)Real Brasileño",
            "3)Peso Chileno",
            "4)Peso Uruguayo"
    ]
    print(*menu, sep="\n")
    x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()
    if x == "1":
        get_dollar("cotizaciones/eur")
    elif x == "2":
        get_dollar("cotizaciones/brl")
    elif x == "3":
        get_dollar("cotizaciones/clp")
    elif x == "4":
        get_dollar("cotizaciones/uyu")
    else:
        clean_terminal()
        get_other_currency()

"""Current Value Options""" ##########################################################




def currency_conversion_menu():
    ...



















if __name__ == "__main__":
    main()
