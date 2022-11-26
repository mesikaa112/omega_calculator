from math import pow
from Validation import *
from substring_number import substring_number


def plus_calculate(equation: str, index: int) -> float:
    """
    this method calculates the addition between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_plus_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(operand1 + operand2)


def minus_calculate(equation: str, index: int) -> float:
    """
    this method calculates the subtraction between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_minus_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(operand1 - operand2)


def mul_calculate(equation: str, index: int) -> float:
    """
    this method calculates the multiply between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_multiply_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(operand1 * operand2)


def div_calculate(equation: str, index: int) -> float:
    """
    this method calculates the division between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_divide_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(operand1 / operand2)


def pow_calculate(equation: str, index: int) -> float:
    """
    this method calculates the power between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_power_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(pow(operand1, operand2))


def mod_calculate(equation: str, index: int) -> float:
    """
    this method calculates the modulo between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_modulo_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(operand1 % operand2)


def max_calculate(equation: str, index: int) -> float:
    """
    this method calculates the maximum between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_maximum_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(max(operand1, operand2))


def min_calculate(equation: str, index: int) -> float:
    """
    this method calculates the minimum between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_minimum_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float(min(operand1, operand2))


def avg_calculate(equation: str, index: int) -> float:
    """
    this method calculates the average between two operands
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_average_validate(equation, index):
        operand1, operand2 = substring_number(equation, index)
        return float((operand1 + operand2) / 2)


def neg_calculate(equation: str, index: int) -> float:
    """
    this method calculates the negative of an operand
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_negative_validate(equation, index):
        operand = substring_number(equation, index)[1]
        return float(-operand)


def fac_calculate(equation: str, index: int) -> float:
    """
    this method calculates the factorial of an operand
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: the result of the calculation in float type
    """
    if check_factorial_validate(equation, index):
        operand = substring_number(equation, index)[0]
        return float(factorial_calc(int(operand)))


def factorial_calc(operand: int) -> int:
    """
    this method is a recursive method that calculate the factorial of a number
    :return: the result of the calculation
    """
    if operand == 1:
        return 1
    return operand * factorial_calc(operand - 1)
