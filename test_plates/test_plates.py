from plates import is_valid

def test_initial_letters():
    for plate in ["C523", "C236", "D922"]:
        assert is_valid(plate) == False

def test_length():
    for plate in ["C", "COMPUTER50", "HARVARD"]:
        assert is_valid(plate) == False

def test_numbers_rules():
    for plate in ["CS05", "DAN3P"]:
        assert is_valid(plate) == False

def test_no_punctuation():
    for plate in ["CS'50", "CS 50", "DANI_30"]:
        assert is_valid(plate) == False

def test_validplate():
    for plate in ["DANI40", "PRO2", "CA"]:
        assert is_valid(plate) == True








