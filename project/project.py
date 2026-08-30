#Libraries used in the program
import sys
import time
import os
import requests
from datetime import datetime, timezone

API_URL = "https://dolarapi.com/v1/"

#Menus available to be used by other functions
currency_data_and_name =[
                          {"id": 1, "name": "1)Dólar Oficial", "route": "dolares/oficial", "package": lambda: print_currency_value(get_rate(["route"]))},
                          {"id": 2, "name": "2)Dólar Blue", "route": "dolares/blue"},
                          {"id": 3, "name": "3)Dólar Bolsa / MEP", "route": "dolares/bolsa"},
                          {"id": 4, "name": "4)Dólar Tarjeta", "route": "dolares/tarjeta"},
                          {"id": 5, "name": "5)Dólar Cripto", "route": "dolares/cripto"},
                          {"id": 6, "name": "6)Euro", "route": "cotizaciones/eur"},
                          {"id": 7, "name": "7)Real Brasileño", "route": "cotizaciones/brl"},
                          {"id": 8, "name": "8)Peso Chileno", "route": "cotizaciones/clp"},
                          {"id": 9, "name": "9)Peso Uruguayo", "route": "cotizaciones/uyu"},
                          {"id": 10, "name": "10)Main Menu", "route": None}


]

valid_main_menu_options = [
        {"id": "1", "name": "1)Currency Value", "route": lambda: current_currency_value()}

]



#Function used to clean the terminal for the user
def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


#Main Function


def main():
    try:
        while True:
            main_menu()
    except (EOFError, KeyboardInterrupt):
        sys.exit("Closing the program...\n")



#Function used to display menus, then ask the user for an input, then returns that input to the caller function
def menu_displayer(menu_to_display):
    while True:
        for option in menu_to_display:
            print(option["name"], sep="\n")
        user_input = input("Please choose an option (1, 2, 3 ...)").strip().lower()

        if any(str(option["id"]) == user_input for option in menu_to_display):
            clean_terminal()
            return user_input

        else:
            print("Please select a valid option")
            time.sleep(1)
            clean_terminal()

def main_menu():
    user_input = menu_displayer(valid_main_menu_options)

    selected_option = menu_option_matcher(valid_main_menu_options, user_input)
    selected_option["function_to_call"]()

#matches the user input to the menu option, then, if valid, returns the user input to the caller
def menu_option_matcher(valid_menu, user_input_):
    for opt in valid_menu:
        if str(opt["id"]) == user_input_:
            return opt
    return None






#Function in charge of getting the current value of the currency

def current_currency_value():
    while True:
        user_input = menu_displayer(currency_data_and_name).strip().lower()

        selected_currency = menu_option_matcher(currency_data_and_name, user_input)

        if selected_currency["id"] == 10:
            break

        else:
            data = get_rate(selected_currency["route"])
            print_currency_value(data)
            input("\nPress enter to continue...")
            clean_terminal()



#function used to convert ISO 8601 string format to minutes ago
def iso_format_converter(isostring):
    # convert ISO 8601 string format to minutes ago
    datestripped = datetime.fromisoformat(isostring.replace("Z", "+00:00"))
    now_utc = datetime.now(timezone.utc)
    difference = now_utc - datestripped

    minutes_ago = int(difference.total_seconds() / 60)

    #returns minutes_ago in a more user-friendly format
    if minutes_ago == 0:
        return "Just now"
    elif minutes_ago == 1:
        return "A minute ago"
    else:
        return f"{minutes_ago} minutes ago"


#Function used to get the current value of the currency, returning it as a dictionary in order to be used by other functions


def get_rate(currency_key):

    currency_key = currency_key.strip().lower()
    url = f"{API_URL}{currency_key}"

    try:
        request_json = requests.get(url)
        request_json.raise_for_status()

        # currency_data variable used to store the requests.get json
        currency_data = request_json.json()
        type_buy = currency_data.get("compra", "N/A")
        type_sell = currency_data.get("venta", "N/A")
        coin_name = currency_data["nombre"]
        coin = currency_data["moneda"]

        #calls iso_format_converter with currency_data["fechaActualizacion"] as parameter in order to be converted do a "minutes ago" format
        minutes_ago = iso_format_converter(currency_data["fechaActualizacion"])

        return {"type_buy": type_buy,
                "type_sell": type_sell,
                "coin_name": coin_name,
                "coin": coin,
                "minutes_ago": minutes_ago
                }

    except requests.exceptions.RequestException as e:
        return {
            "type_buy": "Error",
            "type_sell": "Error",
            "coin_name": "API Unreachable",
            "coin": "",
            "minutes_ago": "N/A",
        }




#prints the currency value in a user-friendly format
def print_currency_value(currency_data):
    clean_terminal()
    print(f"{currency_data['coin']} {currency_data['coin_name']}",
          f"Sale Value: {currency_data['type_sell']}",
          f"Purchase Value: {currency_data['type_buy']}",
          f"Last updated: {currency_data['minutes_ago']}",
          sep="\n"
          )



if __name__ == "__main__":
    main()
