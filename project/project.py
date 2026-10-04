import sys
import time
import os
import requests
import math
from datetime import datetime, timezone

API_URL = "https://dolarapi.com/v1/"

# Menus available to be used by other functions in this program

MAIN_MENU_OPTIONS = [
    {"id": 1, "name": "Value of Currencies", "action": "view_rates"},
    {"id": 2, "name": "Currency Conversion", "action": "currency_conversion"},
    {"id": 3, "name": "Financial Calculators", "action": "calculators"},
    {"id": 4, "name": "Exit", "action": "exit"}
]

CALCULATOR_OPTIONS = [
    {"id": 1, "name": "Savings Calculator", "action": "savings"},
    {"id": 2, "name": "Breach Calculator", "action": "exchange_gap"},
    {"id": 3, "name": "Buy/sell spread calculator", "action": "spread"},
    {"id": 4, "name": "Back to Main Menu", "action": "exit"}

]

BREACH_CALCULATOR_MENU = [
    {"id": 1, "name": "Blue Dollar", "route": "dolares/blue"},
    {"id": 2, "name": "Stoch Market / MEP Dollar", "route": "dolares/bolsa"},
    {"id": 3, "name": "Card Dollar", "route": "dolares/tarjeta"},
    {"id": 4, "name": "Back to Financial Calculators", "route": "exit"}
]

SPREAD_CALCULATOR_MENU = [
    {"id": 1, "name": "Blue Dollar", "route": "dolares/blue"},
    {"id": 2, "name": "Stock Market / MEP Dollar", "route": "dolares/bolsa"},
    {"id": 3, "name": "Card Dollar", "route": "dolares/tarjeta"},
    {"id": 4, "name": "Cripto Dollar", "route": "dolares/cripto"},
    {"id": 5, "name": "Euro", "route": "cotizaciones/eur"},
    {"id": 6, "name": "Back to Financial Calculators", "route": "exit"}
]


CURRENCY_DATA_AND_NAME = [
    {"id": 1, "name": "Official Dollar", "route": "dolares/oficial"},
    {"id": 2, "name": "Blue Dollar", "route": "dolares/blue"},
    {"id": 3, "name": "Stock Market / MEP Dollar", "route": "dolares/bolsa"},
    {"id": 4, "name": "Card Dollar", "route": "dolares/tarjeta"},
    {"id": 5, "name": "Cripto Dollar", "route": "dolares/cripto"},
    {"id": 6, "name": "Euro", "route": "cotizaciones/eur"},
    {"id": 7, "name": "Brasilian Real", "route": "cotizaciones/brl"},
    {"id": 8, "name": "Chilean Peso", "route": "cotizaciones/clp"},
    {"id": 9, "name": "Uruguayan Peso", "route": "cotizaciones/uyu"},
    {"id": 10, "name": "Back to Main Menu", "route": "exit"},
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
def menu_displayer(menu_to_display, optional_string=None, item_suffix=None, print_welcome_flag=None):
    while True:

        if optional_string:
            print_header(optional_string)

        if print_welcome_flag:
            print_welcome()

        for option in menu_to_display:
            if item_suffix and option.get("route") != "exit" and option.get("action") != "exit":
                print(f"{option['id']}) {option['name']} {item_suffix}")

            else:
                print(f"{option['id']}) {option['name']}")

        user_input = input("Please choose an option (1, 2, 3 ...)").strip().lower()

        if any(str(option["id"]) == user_input for option in menu_to_display):
            clean_terminal()
            return user_input

        else:
            print("Please select a valid option")
            time.sleep(1)
            clean_terminal()


def print_header(title):
    title = title.upper()
    width = 51
    print("=" * width)
    print(title.center(width))
    print("=" * width + "\n")


def print_welcome():
    print("Blue app is a financial tool that fetches real-time exchange rates")
    print("from DolarApi to convert currencies and calculate spreads, savings")
    print("and exchange gaps.\n")


def main_menu():
    clean_terminal()
    user_input = menu_displayer(MAIN_MENU_OPTIONS, "BLUEAPP", None, True)
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
        user_input = menu_displayer(CURRENCY_DATA_AND_NAME, "Currency Value Viewer")

        selected_currency = menu_option_matcher(CURRENCY_DATA_AND_NAME, user_input)

        if not selected_currency:
            continue

        if selected_currency["route"] == "exit":
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
    if not isinstance(isostring, str) or not isostring.strip():
        return "Unknown"

    try:
        formatted_string = isostring.replace("Z", "+00:00")
        datestripped = datetime.fromisoformat(formatted_string)
    except ValueError:
        return "Unknown"

    if datestripped.tzinfo is None:
        return "Unknown"

    now_utc = datetime.now(timezone.utc)
    difference = now_utc - datestripped

    minutes_ago = max(0, int(difference.total_seconds() / 60))

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

    request_json = requests.get(url, timeout=10)
    request_json.raise_for_status()

    return request_json.json()


def parse_currency_payload(raw_data):
    date_str = raw_data.get("fechaActualizacion")
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
    print_header("CURRENCY VALUE")
    print(f"Coin           : {currency_data['coin']} {currency_data['coin_name']}",
          "-" * 51,
          f"Sale Value     : {currency_data['type_sell']}",
          f"Purchase Value : {currency_data['type_buy']}",
          "-" * 51,
          f"Last updated   : {currency_data['minutes_ago']}",
          "-" * 51,
          sep="\n"
          )


# --! Conversion functions !--#

def print_converted_currency_value(converted, currency_1, currency_2, amount_to_convert):
    clean_terminal()
    print_header("CURRENCY CONVERSION RESULT")

    rate = (
        rate_value(currency_1, "compra")
        / rate_value(currency_2, "venta")
    )

    name_1 = f"{currency_1['moneda']} ({currency_1['nombre']})" if currency_1['moneda'] == "USD" else currency_1['moneda']
    name_2 = f"{currency_2['moneda']} ({currency_2['nombre']})" if currency_2['moneda'] == "USD" else currency_2['moneda']

    print(f"  Amount entered    : {amount_to_convert:.2f} {name_1}")
    print(f"  Target Currency   : {name_2}\n")
    print("-" * 51 + "\n")
    print(f"  Exchange rate     : 1 {name_1} = {rate:,.2f} {name_2}")
    print(f"  Total to receive  : ${converted:,.2f} {name_2}\n")
    print("-" * 51)
    print("  [i]Real-time rate fetched from DolarApi.")
    print("=" * 51 + "\n")

    input("Press enter to continue...")
    clean_terminal()


def currency_selection_checker(input_1, input_2):
    if input_1["route"] == input_2["route"]:
        return False
    else:
        return True


def amount_input(input_type):
    prompts = {
        "currency": "How much do you wish to convert?\n",
        "calculate": "How much USD are you paying or consuming?\n",
    }

    if input_type not in prompts:
        raise ValueError("Unknown input type")

    while True:
        try:
            amount = float(input(prompts[input_type]))

            if not math.isfinite(amount):
                raise ValueError

            if amount < 0:
                raise ValueError

            if input_type == "calculate" and amount == 0:
                raise ValueError

            if input_type == "calculate":
                clean_terminal()

            return amount
        except ValueError:
            print("Please enter a valid amount")


def rate_value(currency, field):
    value = float(currency[field])

    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"Invalid exchange rate: {field}")

    return value


def calculate_conversion(currency_1, currency_2, amount_to_convert):
    rate_value_1 = rate_value(currency_1, "compra")
    rate_value_2 = rate_value(currency_2, "venta")
    return (rate_value_1 * amount_to_convert) / rate_value_2


def currency_converter(currency_1, currency_2):
    try:
        rate_value(currency_1, "compra")
        rate_value(currency_2, "venta")

        amount_to_convert = amount_input("currency")

        converted = round(calculate_conversion(currency_1, currency_2, amount_to_convert), 4)

        print_converted_currency_value(converted, currency_1, currency_2, amount_to_convert)

    except (KeyError, TypeError, ValueError):
        print("Could not process exchange rates. Please try again later.")
        input("Press enter to continue...")
        clean_terminal()


def currency_conversion():
    while True:
        user_input_1 = menu_displayer(CURRENCY_DATA_AND_NAME, "Currency to convert from:")
        selected_currency_1 = menu_option_matcher(CURRENCY_DATA_AND_NAME, user_input_1)
        if not selected_currency_1 or selected_currency_1["route"] == "exit":
            break

        user_input_2 = menu_displayer(CURRENCY_DATA_AND_NAME, "Currency to convert to:\n")
        selected_currency_2 = menu_option_matcher(CURRENCY_DATA_AND_NAME, user_input_2)
        if not selected_currency_2 or selected_currency_2["route"] == "exit":
            break

        if not currency_selection_checker(selected_currency_1, selected_currency_2):
            print("Please select a different currency to convert to")
            time.sleep(1.5)
            clean_terminal()
            continue

        try:
            currency_1 = get_rate(selected_currency_1["route"])
            currency_2 = get_rate(selected_currency_2["route"])

            currency_converter(currency_1, currency_2)
            break

        except requests.RequestException as e:
            print(f"Error: Could not fetch currency data. ({e})")
            time.sleep(2)
            clean_terminal()
            break


def calculator_options():
    while True:
        user_input = menu_displayer(CALCULATOR_OPTIONS, "Financial Calculators")
        selected_option = menu_option_matcher(CALCULATOR_OPTIONS, user_input)

        if not selected_option or selected_option["action"] == "exit":
            return
        route_calculator_options(selected_option)


def route_calculator_options(selected_option):
    if selected_option["action"] == "savings":
        savings_calculator()
    elif selected_option["action"] == "exchange_gap":
        breach_calculator()
    elif selected_option["action"] == "spread":
        buy_sell_spread_calculator()
    elif selected_option["action"] == "exit":
        return


def calculate_savings(amount, card_rate, mep_rate):
    return round(amount * (card_rate - mep_rate), 2)


def savings_calculator():
    try:
        usd_amount = amount_input("calculate")

        card_rate = rate_value(get_rate("dolares/tarjeta"), "venta")
        mep_rate = rate_value(get_rate("dolares/bolsa"), "venta")

        price_card = usd_amount * card_rate
        price_mep = usd_amount * mep_rate
        savings = calculate_savings(usd_amount, card_rate, mep_rate)

        print_header("USD SAVINGS CALCULATOR")
        print(f"  Purchase/Expense amount: {usd_amount:.2f} USD\n")
        print(f"  • Direct Card Payment(ARS)   : ${price_card:,.2f} ARS")
        print(f"  • Payment with MEP Dollars  : ${price_mep:,.2f} ARS")
        print("-" * 51 + "\n")

        if savings > 0:
            percentage = (savings / price_card) * 100
            print("  >>> RECOMMENDED OPTION: DÓLAR MEP <<<")
            print(f"  Estimated savings: ${savings:,.2f} ARS ({percentage:.1f}% off)\n")
            print("  [Tip] Pay your credit card statement in USD before the due")
            print("        date using MEP dollars to avoid ARS tax perception\n")

        elif savings < 0:
            print("  >>> RECOMMENDED OPTION: DIRECT CARD PAYMENT <<<")
            print(f"  Estimated savings: ${abs(savings):,.2f} ARS\n")
            print("  [Tip] Card rate is currently cheaper than buying MEP.")
        else:
            print("  Both options cost the same.")

        input("Press enter to continue...")
        clean_terminal()
    except (KeyError, TypeError, ValueError, requests.RequestException):
        print("Service temporarily unavailable. Please try again later.")
        input("Press enter to continue...")
        clean_terminal()


def calculate_breach(oficial_value, type_value):
    difference = type_value - oficial_value
    gap_percentage = (difference / oficial_value) * 100

    return round(gap_percentage, 2), round(difference, 2)


def breach_calculator():

    while True:
        user_input = menu_displayer(BREACH_CALCULATOR_MENU,
                                    "Breach calculation Options:", "vs Dólar Oficial")
        selected_option = menu_option_matcher(BREACH_CALCULATOR_MENU, user_input)

        if not selected_option or selected_option["route"] == "exit":
            break
        try:
            official = get_rate("dolares/oficial")
            target = get_rate(selected_option["route"])

            official_sell = official["venta"]
            target_sell = rate_value(target, "venta")

            gap_percentage, difference_ars = calculate_breach(official_sell, target_sell)

            print_breach_results(
                selected_option["name"],
                official_sell,
                target_sell,
                gap_percentage,
                difference_ars
            )

        except (KeyError, TypeError, ValueError, requests.RequestException):
            print("[i] Could not fetch or process exchange rate data. Please try again.")


def print_breach_results(target_name, official_sell, target_sell, gap_percentage, difference_ars):
    clean_terminal()
    print_header(f"EXCHANGE GAP: Official vs. {target_name}")

    # Categorize status based on gap magnitude
    if gap_percentage > 30:
        status = "High"
    elif gap_percentage > 15:
        status = "Moderate"
    else:
        status = "Low"

    print(f"  Official USD (Sell)  : ${official_sell:,.2f} ARS")
    print(f"  {target_name} (Sell)  : ${target_sell:,.2f} ARS")
    print("-" * 51)
    print(f"  PERCENTAGE GAP    : {gap_percentage:+.2f}%")
    print(f"  DIFFERENCE        : ${difference_ars:,.2f} ARS per USD")
    print(f"  GAP STATUS        : {status}")
    print("  [i] Exchange gap measures the cost difference relative")
    print("      to the official regulated exchange rate.")
    print("=" * 51)

    input("\nPress enter to continue...")
    clean_terminal()


def calculate_spread(selected_option):
    currency = get_rate(selected_option)
    currency_buy = rate_value(currency, "compra")
    currency_sell = rate_value(currency, "venta")

    nominal_spread = currency_sell - currency_buy
    percentage_spread = ((currency_sell - currency_buy) / currency_sell) * 100

    return nominal_spread, percentage_spread, currency_buy, currency_sell


def buy_sell_spread_calculator():

    while True:
        user_input = menu_displayer(SPREAD_CALCULATOR_MENU, "Select rate to check spread")
        selected_option = menu_option_matcher(SPREAD_CALCULATOR_MENU, user_input)

        if not selected_option or selected_option["route"] == "exit":
            break

        try:
            nominal_spread, percentage_spread, price_buy, price_sell = calculate_spread(
                selected_option["route"])

            print_spread_results(
                selected_option["name"],
                price_buy,
                price_sell,
                nominal_spread,
                percentage_spread
            )

        except (KeyError, TypeError, ValueError, requests.RequestException):
            print("Service temporarily unavailable. Please try again later.")


def print_spread_results(currency_name, compra_rate, venta_rate, nominal_spread, percentage_spread):
    clean_terminal()
    print_header(f"SPREAD CALCULATOR - {currency_name.upper()}")

    print(f"  Buy Price  (User sells USD)  : ${compra_rate:,.2f} ARS")
    print(f"  Sell Price (User buys USD))  : ${venta_rate:,.2f} ARS")
    print(f"-" * 51)
    print(f"  NOMINAL SPREAD     : ${nominal_spread:,.2f} ARS")
    print(f"  PERCENTAGE MARGIN  : {percentage_spread:.2f}%")
    print("-" * 51)
    print("  [i] The spread represents the fee or margin retained")
    print("      by intermediaries in a round trip transaction.")
    print("=" * 51)

    input("\nPress enter to continue...")
    clean_terminal()


if __name__ == "__main__":
    main()
