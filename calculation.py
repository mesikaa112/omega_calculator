from math import pow
from validation import *


def plus_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the addition between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        return float(float(operand1) + float(operand2))
    else:
        raise DecimalPointError()


def minus_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the subtraction between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        return float(float(operand1) - float(operand2))
    else:
        raise DecimalPointError()


def mul_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the multiply between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        return float(float(operand1) * float(operand2))
    else:
        raise DecimalPointError()


def div_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the division between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        # if there isn't divide by 0
        if operand2 != '0' and operand2 != '0.0':
            return float(float(operand1) / float(operand2))
        else:
            raise DivideError("There is an ERROR! you can't divide by zero")
    else:
        raise DecimalPointError()


def pow_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the power between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        return float(pow(float(operand1), float(operand2)))
    else:
        raise DecimalPointError()


def mod_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the modulo between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        if operand2 != '0' and operand2 != '0.0':
            return float(float(operand1) & float(operand2))
        else:
            raise DivideError("There is an ERROR! you can't divide by zero")
    else:
        raise DecimalPointError()


def max_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the maximum between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        if operand1 > operand2:
            return float(operand1)
        else:
            return float(operand2)
    else:
        raise DecimalPointError()


def min_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the minimum between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        if operand1 < operand2:
            return float(operand1)
        else:
            return float(operand2)
    else:
        raise DecimalPointError()


def avg_calculate(operand1: str, operand2: str) -> float:
    """
    this method calculates the average between two operands
    :param operand1: the operand1 in str type
    :param operand2: the operand2 in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand1) and check_decimal_point_validate(operand2):
        return float((float(operand1) + float(operand2)) / 2)
    else:
        raise DecimalPointError()


def fac_calculate(operand: str) -> float:
    """
    this method calculates the factorial of an operand
    :param operand: the operand in str type
    :return: the result of the calculation in float type
    """
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


def sum_calculate(operand: str):
    """
    this method calculates the sum of a few operands
    :param operand: the operand in str type
    :return: the result of the calculation in float type
    """
    if check_decimal_point_validate(operand):
        return float(sum_calc(substring_float_to_int(operand)))
    else:
        raise SumError("\nthere is an ERROR! you can't do Sum on a float number")


def sum_calc(operand: int) -> int:
    """
    this method calculates the sum of a few operands
    :return: the result of the calculation
    """
    str_operand = str(operand)
    if str_operand[0] == '-':
        str_operand = str_operand[1:]
    result = 0
    for num in str_operand:
        result += int(num)
    return result


def calculate_sub_equation(operand1: str, operator: str, operand2: str) -> float:
    """
    this method gets a sub equation from the big equation and calculate it
    :param operand1: operand1 in str type
    :param operator: the operator in the equation in str type
    :param operand2: operand1 in str type
    :return: the calculate of the sub equation
    """
    sub_equation = [operand1, operator, operand2]
    operator_class = get_operator(sub_equation, operator, 1)
    calculation_func = operator_class.calculate()
    if operator in BETWEEN_ONE_OPERATORS:
        if BETWEEN_ONE_OPERATORS.get(operator) == "left":
            return calculation_func(operand2)
        else:
            return calculation_func(operand1)

    if operator in BETWEEN_TWO_OPERATORS:
        return calculation_func(operand1, operand2)
