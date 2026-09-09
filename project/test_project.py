import pytest

from project import menu_displayer, MAIN_MENU_OPTIONS, main_menu, menu_option_matcher, current_currency_value, iso_format_converter, get_rate, print_currency_value



# !--- Test for main_menu --! #

def test_main_menu_currency():
    assert main_menu("2") == "Closing the program...\n"


