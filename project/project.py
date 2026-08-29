import sys
import re
import time
import os
import json
import requests
from datetime import datetime, timezone


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
    while True:
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
            print("Invalid option. Please try again.\n")










"""Current Value Options""" ##########################################################
def current_value_menu():
    #Opens up a menu including the options for quoting specific currency types, then, according to the user input, calls a function which returns the current value of this currency type
    valid = {

        "1": "dolares/oficial",
        "2": "dolares/blue",
        "3": "dolares/bolsa",
        "4": "dolares/tarjeta",
        "5": "dolares/cripto"

    }


    menu = ["1)Dólar Oficial",
            "2)Dólar Blue",
            "3)Dólar MEP / Bolsa",
            "4)Dólar Tarjeta",
            "5)Dólar Cripto",
            "6)Other currencies:",
            "7)Main Menu"
    ]


    while True:
        print(*menu, sep="\n")
        x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()

        if x in valid:
            get_rate(valid[x])
            print_currency_value(get_rate)
            break

        elif x == "6":
            clean_terminal()
            get_other_currency()
            break

        elif x == "7":
            print("Returning to main menu...")
            time.sleep(1.5)
            clean_terminal()
            return

        else:
            print("Please input a valid option.")
            time.sleep(0.5)





#########################
def get_rate(currency_key):

    currency_key = currency_key.strip().lower()

    #type of currencies available
    currency_key_list = ["dolares/oficial",
                 "dolares/blue",
                 "dolares/bolsa",
                 "dolares/tarjeta",
                 "dolares/cripto",
                 "cotizaciones/clp",
                 "cotizaciones/eur",
                 "cotizaciones/brl",
                 "cotizaciones/uyu"
                 ]

    if currency_key in currency_key_list:
        try:
            url = f"https://dolarapi.com/v1/{currency_key}"
            pre_type = requests.get(url)
            # o = variable used to store the requests.get json
            o = pre_type.json()
            type_buy = o["compra"]
            type_sell = o["venta"]
            coin_name = o["nombre"]
            coin = o["moneda"]

            #convert ISO 8601 string format to minutes ago
            datestripped = datetime.fromisoformat(o["fechaActualizacion"])
            now_utc = datetime.now(timezone.utc)
            difference = now_utc - datestripped

            minutes_ = int(difference.total_seconds() / 60)

            if minutes_ == 0:
                minutes_ = "Just now"
            elif minutes_ == 1:
                minutes_ = "A minute ago"
            else:
                minutes_ = f"{minutes_} minutes ago"

                #I saved this directly in the global variable currency_data so that i could extract this data anytime I want from any function I want to, also making it available to be extracted from third-party programs
            currency_data = {"type_buy": type_buy,
                "type_sell": type_sell,
                "coin_name": coin_name,
                "coin": coin,
                "minutes_": minutes_
                }
            return currency_data





        except requests.RequestException:
            sys.exit("Connection Error")






def print_currency_value(s):
        #prints the currency value, using the data from the global currency_data variable

        clean_terminal()
        print(f"{s["coin"]} {s["coin_name"]}",
                f"Sale Value: {s["type_sell"]}",
                f"Purchase Value: {s["type_buy"]}",
                f"Last updated: {s["minutes_"]}",
                sep="\n"
                )
        while True:
            answer = input("Do you wish to do something else? (y/n) ").strip().lower()
            if answer == "y":
                print("Going back to the main menu...")
                time.sleep(1)
                clean_terminal()
                return
            elif answer == "n":
                clean_terminal()
                sys.exit("Closing the program...")
            else:
                clean_terminal()





def get_other_currency():
    valid = {
        "1": "cotizaciones/eur",
        "2": "cotizaciones/brl",
        "3": "cotizaciones/clp",
        "4": "cotizaciones/uyu"
    }

    menu = ["1)Euro",
            "2)Real Brasileño",
            "3)Peso Chileno",
            "4)Peso Uruguayo"
    ]

    while True:
        print(*menu, sep="\n")
        x = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()
        if x in valid:
            get_rate(valid[x])
            print_currency_value(currency_data)

        clean_terminal()
        print("Invalid option. Please try again. \n")


"""Current Value Options""" ##########################################################




"""def currency_conversion_menu():
    menu = ["1)Dólar Blue",
          "2)Dólar Oficial",
          "3)Dólar Bolsa",
          "4)Dólar Tarjeta",
          "5)Dólar Cripto",
          "6)Euro",
          "7)Real Brasileño",
          "8)Peso Chileno",
          "9)Peso Uruguayo"
          ]
    valid = {
            "1": "dolares/oficial",
            "2": "dolares/blue",
            "3": "dolares/bolsa",
            "4": "dolares/tarjeta",
            "5": "dolares/cripto",
            "6": "cotizaciones/eur",
            "7": "cotizaciones/brl",
            "8": "cotizaciones/clp",
            "9": "cotizaciones/uyu"

    }

    print("Currency to convert from", *menu, sep="\n")
    user_input1 = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()

    if user_input1 in valid:
        get_rate(valid[user_input1])
        to_convert = currency_data["type_sell"]

        print("Currency to convert to", *menu, sep="\n")

        user_input2 = input("Select an option (e.g.: 1, 2 ...) ").strip().lower()


        if user_input2 in valid:
            if user_input2 == user_input1:
                print("please convert to another currency")
                return
        else:
"""




























if __name__ == "__main__":
    main()
