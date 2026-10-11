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
    valid_iso = datetime.now(timezone.utc).isoformat()

    mock_data = {"compra": 1500,
                 "venta": 1400,
                 "casa": "string",
                 "nombre": "Blue",
                 "moneda": "Dolar",
                 "fechaActualizacion": valid_iso
    }

    assert project.parse_currency_payload(mock_data) == {
        "type_buy": mock_data.get("compra", "N/A"),
        "type_sell": mock_data.get("venta", "N/A"),
        "coin_name": mock_data.get("nombre", "N/A"),
        "coin": mock_data.get("moneda", "N/A"),
        "minutes_ago": project.iso_format_converter(valid_iso)
    }


def test_print_currency_value(capsys):
    mock_data = {"coin": "USD",
                 "coin_name": "Blue",
                 "type_sell": 1400,
                 "type_buy": 1500,
                 "minutes_ago": "5 minutes ago"
    }

    project.print_currency_value(mock_data)

    captured = capsys.readouterr()

    assert "USD Blue" in captured.out
    assert "Sale Value: 1400" in captured.out
    assert "Purchase Value: 1500" in captured.out
    assert "Last updated: 5 minutes ago" in captured.out


def test_calculate_conversion():
    dollars = {"compra": 1000, "venta": 1100}
    euros = {"compra": 1200, "venta": 1250}

    assert project.calculate_conversion(dollars,euros, 100) == 80
    assert project.calculate_conversion(dollars, euros, 0) == 0
    assert project.calculate_conversion(dollars, euros, 50) == 40
def test_calculate_savings():
    assert project.calculate_savings(100, 1500, 1200) == 30000
    assert project.calculate_savings(100, 1200, 1500) == -30000
    assert project.calculate_savings(100, 1200, 1200) == 0
    assert project.calculate_savings(3, 100.123, 100) == 0.37

def test_calculate_breach():
    assert project.calculate_breach(1000, 1200) == (20, 200)
    assert project.calculate_breach(1000, 800) == (-20, -200)
    assert project.calculate_breach(1000, 1000) == (0, 0)
    assert project.calculate_breach(3, 4) == (33.33, 1)
