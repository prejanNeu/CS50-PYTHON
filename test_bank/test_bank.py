from bank import value


def test_hello():
    assert value("Hello Prejan")==0
def test_h():
    assert value("Hi, Prejan")== 20
    assert value ("Hey Prejan")== 20

def test_other():
    assert value("Mahalaxmi")==100
    assert value ("Patan_campus")==100