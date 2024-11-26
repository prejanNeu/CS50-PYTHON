from project import prec,associativity,replaceSpace

def test_prec():
    assert prec('^')==3
    assert prec('*') == 2
    assert prec('/') == 2
    assert prec('+') == 1
    assert prec('-') == 1
    assert prec('&') == -1

def test_associativity():
    assert associativity('^') == 'R'
    assert associativity('*') == 'L'
    assert associativity('/') == 'L'
    assert associativity('+') == 'L'
    assert associativity('-') == 'L'
    assert associativity('&') == 'L'

def test_replaceSpace():
    input_expression = "2 * (3 + 4)"
    expected_output = "2*(3+4)"
    assert replaceSpace(input_expression) == expected_output
    input_expression = "  5 * ( 2  - 1 ) "
    expected_output = "5*(2-1)"
    assert replaceSpace(input_expression) == expected_output
    input_expression = ""
    expected_output = ""
    assert replaceSpace(input_expression) == expected_output
    input_expression = "a + b / c - d^2"
    expected_output = "a+b/c-d^2"
    assert replaceSpace(input_expression) == expected_output