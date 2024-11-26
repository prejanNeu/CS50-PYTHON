from seasons import returnIntoMinute


def test_minutes():
    assert returnIntoMinute("2005-03-11")=="Nine million, nine hundred four thousand, three hundred twenty minutes"
    assert returnIntoMinute("2003-03-23")=="Ten million, nine hundred thirty-nine thousand, six hundred eighty minutes"

