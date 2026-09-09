import pytest
from datetime import timezone, datetime
import project


def test_iso_formtat_converter():
    now_iso = datetime.now(timezone.utc).isoformat()
    assert project.iso_format_converter(now_iso) == "Just now"



def test_menu_option_matcher():
