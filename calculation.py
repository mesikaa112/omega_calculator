from math import pow
from validation import *


def plus_calculate(equation: str, index: int) -> float:
    """
    this method calculates the addition between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_plus_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(float(operand1) + float(operand2))
        else:
            raise DecimalPointError()


def minus_calculate(equation: str, index: int) -> float:
    """
    this method calculates the subtraction between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_minus_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(float(operand1) - float(operand2))
        else:
            raise DecimalPointError()


def mul_calculate(equation: str, index: int) -> float:
    """
    this method calculates the multiply between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_multiply_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(float(operand1) * float(operand2))
        else:
            raise DecimalPointError()


def div_calculate(equation: str, index: int) -> float:
    """
    this method calculates the division between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_divide_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(float(operand1) / float(operand2))
        else:
            raise DecimalPointError()


def pow_calculate(equation: str, index: int) -> float:
    """
    this method calculates the power between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_power_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(pow(float(operand1), float(operand2)))
        else:
            raise DecimalPointError()


def mod_calculate(equation: str, index: int) -> float:
    """
    this method calculates the modulo between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_modulo_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float(float(operand1) % float(operand2))
        else:
            raise DecimalPointError()


def max_calculate(equation: str, index: int) -> float:
    """
    this method calculates the maximum between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_maximum_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            if operand1 > operand2:
                return float(operand1)
            else:
                return float(operand2)
        else:
            raise DecimalPointError()


def min_calculate(equation: str, index: int) -> float:
    """
    this method calculates the minimum between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_minimum_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            if operand1 < operand2:
                return float(operand1)
            else:
                return float(operand2)
        else:
            raise DecimalPointError()


def avg_calculate(equation: str, index: int) -> float:
    """
    this method calculates the average between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_average_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
            return float((float(operand1) + float(operand2)) / 2)
        else:
            raise DecimalPointError()


def neg_calculate(equation: str, index: int) -> float:
    """
    this method calculates the negative of an operand
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_negative_validate(equation, index):
        operand = substring_number(equation, index)[1]
        if check_decimal_point_validate(operand):
            return float(-float(operand))
        else:
            raise DecimalPointError()


def fac_calculate(equation: str, index: int) -> float:
    """
    this method calculates the factorial of an operand
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_factorial_validate(equation, index):
        operand = substring_number(equation, index)[0]
        if not check_decimal_point_validate(operand):
            raise FactorialError("\nthere is an ERROR! you can't do Factorial on float number")
        else:
            return float(factorial_calc(substring_float_to_int(operand)))


def factorial_calc(operand: int) -> int:
    """
    this method calculates the factorial of a number
    :return: the result of the calculation
    """
    result = 1
    for num in range(1, operand + 1):
        result *= num
    return result
