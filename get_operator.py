from operator_classes import *
import validation


def get_operator(equation: list, operator: str, index: int):
    """
    this method find which operator is the operator in the str type and return an object of it
    :param equation: the equation in str type
    :param operator: operator in str type
    :param index: the index of the operator in the equation
    :return: an operator object that suits to the operator
    """
    if operator == '+':
        operator = Plus(equation, index)
    elif operator == '-':
        operator = Minus(equation, index)
    elif operator == '*':
        operator = Multiply(equation, index)
    elif operator == '/':
        operator = Divide(equation, index)
    elif operator == '^':
        operator = Power(equation, index)
    elif operator == '%':
        operator = Modulo(equation, index)
    elif operator == '$':
        operator = Maximum(equation, index)
    elif operator == '&':
        operator = Minimum(equation, index)
    elif operator == '@':
        operator = Average(equation, index)
    elif operator == '~':
        operator = Negative(equation, index)
    elif operator == '!':
        operator = Factorial(equation, index)
    elif operator == '#':
        operator = Sum(equation, index)
    return operator


def get_between_two_operator_validation(operator: str):
    """
    this method find the relevant function of validation for the operator
    :param operator: the operator in str type
    :return: the relevant function of validation for the operator
    """
    if operator == '+':
        return validation.check_plus_validate
    elif operator == '-':
        return validation.check_minus_validate
    elif operator == '*':
        return validation.check_multiply_validate
    elif operator == '/':
        return validation.check_divide_validate
    elif operator == '^':
        return validation.check_power_validate
    elif operator == '%':
        return validation.check_modulo_validate
    elif operator == '$':
        return validation.check_maximum_validate
    elif operator == '&':
        return validation.check_minimum_validate
    elif operator == '@':
        return validation.check_average_validate


def get_between_one_operator_validation(operator: str):
    """
    this method find the relevant function of validation for the operator
    :param operator: the operator in str type
    :return: the relevant function of validation for the operator
    """
    if operator == '~':
        return validation.check_negative_validate
    elif operator == '!':
        return validation.check_factorial_validate
    elif operator == '#':
        return validation.check_sum_validate
