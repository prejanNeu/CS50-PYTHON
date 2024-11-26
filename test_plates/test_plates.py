from plates import is_valid

def test_len():
    assert is_valid("CSIT") == True
    assert is_valid("PrejanNeu")==False
    assert is_valid("Prejan")==True

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50")==True

def test_firstnum():
    assert is_valid("123456") == False
    assert is_valid("1rejan") == False

def test_punc():
    assert is_valid("CS.50") == False
def test_num():
    assert is_valid("123456") == False
    assert is_valid("012345") == False

def test_alpnum():
    assert is_valid("1preja") == False
    assert is_valid("CS50j") == False
    assert is_valid("Preja1")==True
    assert is_valid("csit50")==True

def test_alp():
    assert is_valid("Prejan")==True
    assert is_valid("PrejanNeu")==False

