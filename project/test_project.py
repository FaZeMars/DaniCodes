import pytest

from project import menu_displayer, MAIN_MENU_OPTIONS, main_menu, menu_option_matcher, current_currency_value, iso_format_converter, get_rate, print_currency_value



# !--- Test for menu_displayer --! #


def test_main_menu_currency_option(monkeypatch)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    


def test_program_exit(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")
    with pytest.raises(SystemExit) as sample_exception:
        main_menu()

    assert str(sample_exception.value) == "Closing the program...\n"



