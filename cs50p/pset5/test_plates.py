from plates import is_valid

def test_alpha():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("1A") == False
    assert is_valid("11") == False

def test_length():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_number():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("05CS") == False

def test_punct():
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False

