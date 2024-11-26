from um import count

def test_um():
    assert count("um")==1
    assert count('um, prejan')==1
    assert count('Um, i am going um, yumm')==2