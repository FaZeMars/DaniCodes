# Libraries used in the program
import sys
import time
import os
import requests
from datetime import datetime, timezone

API_URL = "https://dolarapi.com/v1/"

# Menus available to be used by other functions

MAIN_MENU_OPTIONS = [
    {"id": 1, "name": "Value of Currencies", "action": "view_rates"},
    {"id": 2, "name": "Currency Conversion", "action": "currency_conversion"},
    {"id": 3, "name": "Calculator Options", "action": "calculators"},
    {"id": 4, "name": "Exit", "action": "exit"}
]

CALCULATOR_OPTIONS = [
    {"id": 1, "name": "Savings Calculator"},
    {"id": 2, "name": "Exchange Rate Gap Calculator"},
    {"id": 3, "name": "Effective Sales Calculator"},

]


currency_data_and_name = [
    {"id": 1, "name": "Dólar Oficial", "route": "dolares/oficial"},
    {"id": 2, "name": "Dólar Blue", "route": "dolares/blue"},
    {"id": 3, "name": "Dólar Bolsa / MEP", "route": "dolares/bolsa"},
    {"id": 4, "name": "Dólar Tarjeta", "route": "dolares/tarjeta"},
    {"id": 5, "name": "Dólar Cripto", "route": "dolares/cripto"},
    {"id": 6, "name": "Euro", "route": "cotizaciones/eur"},
    {"id": 7, "name": "Real Brasileño", "route": "cotizaciones/brl"},
    {"id": 8, "name": "Peso Chileno", "route": "cotizaciones/clp"},
    {"id": 9, "name": "Peso Uruguayo", "route": "cotizaciones/uyu"},
    {"id": 10, "name": "Back to Main Menu", "route": None, "action": "exit"},
]


# Function used to clean the terminal for the user
def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main Function


def main():
    try:
        while True:
            main_menu()
    except (EOFError, KeyboardInterrupt):
        sys.exit("Closing the program...\n")


# Function used to display menus, then ask the user for an input, then returns that input to the caller function
def menu_displayer(menu_to_display, optional_string=None):
    while True:

        if optional_string:
            print(optional_string)

        for option in menu_to_display:
            print(f"{option['id']}) {option['name']}")

        user_input = input("Please choose an option (1, 2, 3 ...)").strip().lower()

        if any(str(option["id"]) == user_input for option in menu_to_display):
            clean_terminal()
            return user_input

        else:
            print("Please select a valid option")
            time.sleep(1)
            clean_terminal()


def main_menu():
    user_input = menu_displayer(MAIN_MENU_OPTIONS)
    selected_option = menu_option_matcher(MAIN_MENU_OPTIONS, user_input)

    if not selected_option:
        return
    route_main_action(selected_option)


def route_main_action(action):
    if action["action"] == "view_rates":
        current_currency_value()

    elif action["action"] == "currency_conversion":
        currency_conversion()

    elif action["action"] == "calculators":
        calculator_options()

    elif action["action"] == "exit":
        sys.exit("Closing the program...\n")



# matches the user input to the menu option, then, if valid, returns the user input to the caller


def menu_option_matcher(valid_menu, user_input_):
    for opt in valid_menu:
        if str(opt["id"]) == user_input_:
            return opt
    return None


# Function in charge of getting the current value of the currency

def current_currency_value():
    while True:
        user_input = menu_displayer(currency_data_and_name)

        selected_currency = menu_option_matcher(currency_data_and_name, user_input)

        if not selected_currency:
            continue

        if selected_currency["action"] == "exit":
            break

        fetch_and_display_currency(selected_currency)

        input("\nPress enter to continue...")
        clean_terminal()


def fetch_and_display_currency(currency):
    try:
        raw_data = get_rate(currency["route"])
        parsed_data = parse_currency_payload(raw_data)
        print_currency_value(parsed_data)
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error: Could not fetch currency data. ({e})")


# function used to convert ISO 8601 string format to minutes ago
def iso_format_converter(isostring):
    # convert ISO 8601 string format to minutes ago
    datestripped = datetime.fromisoformat(isostring.replace("Z", "+00:00"))
    now_utc = datetime.now(timezone.utc)
    difference = now_utc - datestripped

    minutes_ago = int(difference.total_seconds() / 60)

    # returns minutes_ago in a more user-friendly format
    if minutes_ago == 0:
        return "Just now"
    elif minutes_ago == 1:
        return "A minute ago"
    else:
        return f"{minutes_ago} minutes ago"


# Function used to get the current value of the currency, returning it as a dictionary in order to be used by other functions


def get_rate(currency_key):
    url = f"{API_URL}{currency_key.strip().lower()}"

    request_json = requests.get(url)
    request_json.raise_for_status()

    return request_json.json()


def parse_currency_payload(raw_data):
    date_str = raw_data.get("fechaActualizacion", datetime.now().isoformat())
    return {
        "type_buy": raw_data.get("compra", "N/A"),
        "type_sell": raw_data.get("venta", "N/A"),
        "coin_name": raw_data.get("nombre", "N/A"),
        "coin": raw_data.get("moneda", "N/A"),
        "minutes_ago": iso_format_converter(date_str)
    }


# prints the currency value in a user-friendly format
def print_currency_value(currency_data):
    clean_terminal()
    print(f"{currency_data['coin']} {currency_data['coin_name']}",
          f"Sale Value: {currency_data['type_sell']}",
          f"Purchase Value: {currency_data['type_buy']}",
          f"Last updated: {currency_data['minutes_ago']}",
          sep="\n"
          )


def print_converted_currency_value(value_to_print, currency_1, currency_2, amount_to_convert):
    print(f"{amount_to_convert} {currency_1["moneda"]} {currency_1["nombre"]} is {value_to_print} {currency_2["moneda"]} {currency_2["nombre"]}\n")
    input("Press enter to continue...")
    clean_terminal()




#--! Conversion functions !--#

def currency_selection_checker(input_1, input_2):
        if input_1 == input_2:
            return False
        else:
            return True



def currency_converter_input():
    while True:
        try:
            amount_to_convert = int(input("How much to you wish to convert?\n"))
            return amount_to_convert
        except ValueError:
            print("Please enter a valid amount")


def currency_converter(currency_1, currency_2):
    while True:
        try:

            amount_to_convert = currency_converter_input()

            converted = (currency_1["venta"] * amount_to_convert) / currency_2["venta"]
            print_converted_currency_value(converted, currency_1, currency_2, amount_to_convert)
            break

        except requests.RequestException as e:
            print(f"Error: Could not fetch currency data. ({e})")
            return






def currency_conversion():
    while True:
        user_input_1 = menu_displayer(currency_data_and_name, "Currency to convert from:\n")
        selected_currency_1 = menu_option_matcher(currency_data_and_name, user_input_1)
        if selected_currency_1["action"] == "exit":
            break

        user_input_2 = menu_displayer(currency_data_and_name, "Currency to convert to:\n")
        selected_currency_2 = menu_option_matcher(currency_data_and_name, user_input_2)
        if selected_currency_2["action"] == "exit":
            break

        checked = currency_selection_checker(selected_currency_1, selected_currency_2)

        if checked:
            currency_1 = get_rate(selected_currency_1["route"])
            currency_2 = get_rate(selected_currency_2["route"])

            currency_converter(currency_1, currency_2)
            break

        else:
            print("please select a different currency to convert to")
            time.sleep(1)
            clean_terminal()




def calculator_options():
    ...






















if __name__ == "__main__":
    main()
