import pytest
from seasons import Birth

def test_invalid():
    Birth.get("2026-1-2") == "Invalid Date"

