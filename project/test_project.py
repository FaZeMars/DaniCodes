import pytest
from datetime import timezone, datetime
import project


def test_iso_formtat_converter():
    now_iso = datetime.now(timezone.utc).isoformat()
    assert project.iso_format_converter(now_iso) == "Just now"



def test_menu_option_matcher():
    mock_menu = [
        {"id": 1, "name": "Value of Currencies", "action": "view_rates"},
        {"id": 2, "name": "Exit", "action": "exit"}
    ]

    assert project.menu_option_matcher(mock_menu, "1")["action"] == "view_rates"
    assert project.menu_option_matcher(mock_menu, "2")["action"] == "exit"


def test_parse_currency_payload():
    mock_data = [
        



    ]

