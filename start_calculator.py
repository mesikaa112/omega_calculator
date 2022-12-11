from exception import *
from output import *
from substring_number import substring_spaces, add_result_to_equation
from operator import *
from validation import check_unary_minus_validate, check_vaild_chars
from const import *


def start_calculation():
    """
    this method starts the calculation process and takes care on the exceptions
    """
    while True:
        try:
            equation = welcome_output()
            result = calculate(equation)
            result_output(result)
            if end_of_calculation() == "quit":
                goodbye_output()
                break
        except PlusError as error:
            print(error)
        except MinusError as error:
            print(error)
        except MultiplyError as error:
            print(error)
        except DivideError as error:
            print(error)
        except PowerError as error:
            print(error)
        except ModuloError as error:
            print(error)
        except MaximumError as error:
            print(error)
        except MinimumError as error:
            print(error)
        except AverageError as error:
            print(error)
        except NegativeError as error:
            print(error)
        except FactorialError as error:
            print(error)
        except EmptyInputError as error:
            print(error)
        except IndexError as error:
            print(error)
        except DecimalPointError as error:
            print(error)
        except InValidCharsError as error:
            print(error)
        except EOFError as error:
            print(error)


def calculate(equation: str) -> int:
    """
    this method calculates the result of the equation
    :param equation: the equation in str type
    :return: the result of the final calculation in int type
    """
    if equation == "":
        raise EmptyInputError()
    if not check_vaild_chars(equation):
        raise InValidCharsError()
    equation = substring_spaces(equation)
    temp = equation
    result = equation
    while not get_max_priority(equation)[1]:
        operator = get_max_priority(equation)[0]
        operator = get_operator(equation, operator, equation.index(operator))
        result = operator.calculate()
        equation = add_result_to_equation(equation, result, operator.index)
    if temp == equation:
        if not check_decimal_point_validate(equation):
            raise DecimalPointError()
    return result


def get_max_priority(equation: str) -> (str, bool):
    """
    this method find the operator with the biggest priority in the equation
    :param equation: the equation in str type
    :return: the operator with biggest priority in the equation and False if there is an operator like that, True otherwise
    """
    max_priority = 0
    operator = ""
    over_calculating = True
    for char in equation:
        if char == '-':
            if not check_unary_minus_validate(equation, equation.index(char)):
                continue
        if has_key(char):
            over_calculating = False
            if max_priority < OPERATORS_PRIORITY.get(char):
                max_priority = OPERATORS_PRIORITY.get(char)
                operator = char
    return operator, over_calculating


def has_key(char: str) -> bool:
    """
    this method checks in the operator dict if the char in there or not
    :param char: the operator (or other char)
    :return: True if the char is an operator in the OPERATORS_PRIORITY dict, False otherwise
    """
    for key in OPERATORS_PRIORITY.keys():
        if char == key:
            return True
    return False


def get_operator(equation: str, operator: str, index: int) -> Operator:
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
    return operator
