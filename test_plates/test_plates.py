from plates import is_valid

def test_initial_letters():
    for plate in ["CS50", "CS560", "DANI30"]:
        assert is_valid(plate) == True
    for plate in ["50CS", "560CS", "30DANI"]:
        assert is_valid(plate) == False

def test_length():
    for plate in ["C", "COMPUTER50", "HARVARD"]:
        assert is_valid(plate) == False
    for plate in ["C2", "CS50"]:
        assert is_valid(plate) == True

def test_numbers_rules():
    for plate in ["CS50", "CS30", "CS594"]:
        assert is_valid(plate) == True
    for plate in ["CS05", "050CS", "DANI03"]:
        assert is_valid(plate) == False

def test_no_punctuation():
    for plate in ["CS'50", "CS 50", "DANI_30"]
        assert is_valid(plate) == False
    for plate in ["]








