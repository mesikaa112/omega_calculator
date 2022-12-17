from operator_classes import *


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
