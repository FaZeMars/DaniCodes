import pytest
from datetime import timezone, datetime


from project import menu_displayer, MAIN_MENU_OPTIONS, main_menu, menu_option_matcher, current_currency_value, iso_format_converter, get_rate, print_currency_value



def test_iso_formtat_converter():
    now_iso = datetime.now(timezone.utc).isoformat()
    assert iso_format_converter(now_iso) == "Just now"



def test_
