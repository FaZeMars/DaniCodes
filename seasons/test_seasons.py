import pytest
from seasons import Birth

def test_invalid():
    with pytest.raises(ValueError):
        Birth.get("2026-1-2")

