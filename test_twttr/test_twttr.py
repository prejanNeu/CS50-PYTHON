from twttr import shorten


def test_shorten():
    assert shorten("David")=="Dvd"
    assert shorten("Prejan")=="Prjn"

def test_shorten_Lower():
    assert shorten("school")=="schl"
    assert shorten("mahalaxmi")=="mhlxm"
def test_shorten_upper():
    assert shorten("PNNEMPEL")=="PNNMPL"

def test_shorten_punc():
    assert shorten("Pre;@aes")=="Pr;@s"
    assert shorten("*#prejan&")=="*#prjn&"

def test_shorten_num():
    assert shorten("PA32TA5N")=="P32T5N"
    assert shorten ("APPLE1234")=="PPL1234"

