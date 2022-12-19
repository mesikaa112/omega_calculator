import pytest
from exception import *
from validation import *
from start_calculator import *


def test_for_5_simple_syntax_errors():
    with pytest.raises(MissingOperandError):
        calculate("5+")

    with pytest.raises(FactorialError):
        calculate("7.1!")
    #
    with pytest.raises(DecimalPointError):
        calculate("15+2.5.47")

    with pytest.raises(MissingOperandError):
        calculate("9+7+")

    with pytest.raises(MinusError):
        calculate("22^-")


def test_for_jibrish_error():
    with pytest.raises(InValidCharsError):
        calculate("hjtrofjmrvrv")


def test_for_empty_expression_error():
    with pytest.raises(EmptyInputError):
        calculate("")


def test_for_white_spaces_error():
    with pytest.raises(EmptyInputError):
        calculate("\t")

    with pytest.raises(EmptyInputError):
        calculate("\t")

    with pytest.raises(EmptyInputError):
        calculate("\t")

    with pytest.raises(EmptyInputError):
        calculate("\t")

    with pytest.raises(EmptyInputError):
        calculate("\t")

    with pytest.raises(EmptyInputError):
        calculate("\t")


def test_simple_expressions():
    # 1
    answer = calculate("5+9")
    assert answer == "14.0"

    # 2
    answer = calculate("5-2")
    assert answer == "3.0"

    # 3
    answer = calculate("4*3")
    assert answer == "12.0"

    # 4
    answer = calculate("81/9")
    assert answer == "9.0"

    # 5
    answer = calculate("3^3")
    assert answer == "27.0"

    # 6
    answer = calculate("8%3")
    assert answer == "2.0"

    # 7
    answer = calculate("8$9")
    assert answer == "9.0"

    # 8
    answer = calculate("8&9")
    assert answer == "8.0"

    # 9
    answer = calculate("10@2")
    assert answer == "6.0"

    # 10
    answer = calculate("~7")
    assert answer == "-7"

    # 11
    answer = calculate("5!")
    assert answer == "120.0"

    # 12
    answer = calculate("548#")
    assert answer == "17.0"

    # 13
    answer = calculate("5*-3")
    assert answer == "-15.0"

    # 14
    answer = calculate("5.2*4")
    assert answer == "20.8"

    # 15
    answer = calculate("(2+4)*-4")
    assert answer == "-24.0"


def test_for_complicated_expressions():
    # 1
    answer = calculate("(--2+(5$4*(-2^2)     /2)#+1)!")
    assert answer == "24.0"

    # 2
    answer = calculate("        (--3&5)!-110*(~3)+(((2^-1-1)))")
    assert answer == "335.5"

    # 3
    answer = calculate("4 32 @4  #4%    !#!$31---400@45")
    assert answer == "209.5"

    # 4
    answer = calculate("\n\n\n54\n+\t\t44\t*-12 ^2/0.1*25@7")
    assert answer == "1013814.0"

    # 5
    answer = calculate("(7/8+5*0.2  --9--~23&-28@0.1)#!")
    assert answer == "5.109094217170944e+19"

    # 6
    answer = calculate("-~4!+33#/8 + 78 @12 -(45&41&12 + (4*1^55))")
    assert answer == "53.75"

    # 7
    answer = calculate("((----4*----2 /8 +2)!*2)-((~---2.2+8*0.1)!)")
    assert answer == "6.0"

    # 8
    answer = calculate("((14 /2 *3)#*4)/(((-(2^5)#    *-4)&10*8)#)")
    assert answer == "1.5"

    # 9
    answer = calculate("(-- - - 4 )!*2-  12 /(1 2+6&5%4)*4")
    assert answer == "44.30769230769231"

    # 10
    answer = calculate("(78/22)*((484$55)#/2)/(4!-12%13+21)")
    assert answer == "0.859504132231405"

    # 11
    answer = calculate("((---11+5)*(-2))#!+0.55 + (45@55)")
    assert answer == "56.55"

    # 12
    answer = calculate("100@-10---14+20%18*7*4")
    assert answer == "87.0"

    # 13
    answer = calculate("(-4*-3*-2*-6*-0.01)# / 4")
    assert answer == "-2.25"

    # 14
    answer = calculate("(--8-~5)-14*-1+2.1+2.9")
    assert answer == "32.0"

    # 15
    answer = calculate("36.5/0.5-20^3+100%6.6")
    assert answer == "-7926.0"

    # 16
    answer = calculate("((((---4--4)*8)$7@2)/50)*0.7")
    assert answer == "0.063"

    # 17
    answer = calculate("(6!#!#---12-84.4)%4")
    assert answer == "2.5999999999999943"

    # 18
    answer = calculate("14*4*0.000005-------7+~22^2")
    assert answer == "477.00028"

    # 19
    answer = calculate("(12-33+3@2) +- ((4^4*0.3)/22)")
    assert answer == "-21.990909090909092"

    # 20
    answer = calculate("77/7*2/11  - (1$3+23)#!-33")
    assert answer == "-40351.0"
