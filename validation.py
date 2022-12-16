# from substring_number import substring_number, is_number, is_negative_number, substring_float_to_int
from exception import *
from const import *
from operator_classes import *


def check_plus_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of plus sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise PlusError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_unary_minus_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of unary minus sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the unary minus is valid, False otherwise
    """
    if 0 <= index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if not is_number(operand2):
            return False
        elif not is_number(operand1):
            return False
        return True
    else:
        return False


def check_minus_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of minus sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 <= index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if not is_number(operand2):
            raise MinusError()
        elif not is_number(operand1):
            raise MinusError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_multiply_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of multiply sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise MultiplyError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_divide_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of divide sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise DivideError()
        elif operand2 == '0' or operand2 == '0.0':
            raise DivideError("There is an ERROR! you can't divide by zero")
        return True
    else:
        raise IndexError("the index is not valid")


def check_power_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of power sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise PowerError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_modulo_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of modulo sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise ModuloError()
        elif operand2 == '0' or operand2 == '0.0':
            raise ModuloError("There is an ERROR! you can't divide by zero")
        return True
    else:
        raise IndexError("the index is not valid")


def check_maximum_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of maximum sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise MaximumError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_minimum_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of minimum sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise MinimumError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_average_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of average sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise AverageError()
        return True
    else:
        raise AverageError()


def check_negative_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of negative sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 <= index < (len(equation) - 1):
        char, operand = substring_number(equation, index)
        if not is_number(operand) or is_number(char):
            raise NegativeError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_factorial_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of factorial sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 <= index < len(equation):
        operand, char = substring_number(equation, index)
        if (is_number(operand) and is_negative_number(operand)) or is_number(char):
            raise FactorialError()
        if not is_integer(operand):
            raise FactorialError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_sum_validate(equation: list, index: int) -> bool:
    """
    this method check the validation of a sum sign
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 <= index < len(equation):
        operand, char = substring_number(equation, index)
        if (is_number(operand) and is_negative_number(operand)) or is_number(char):
            raise FactorialError()
        if not is_integer(operand):
            raise FactorialError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_decimal_point_validate(operand: str) -> bool:
    """
    this method check if the decimal point in a number is valid
    :param operand: the operand in str type
    :return: True if the decimal point in a number is valid, False otherwise
    """
    count_points = 0
    for char in operand:
        if char == '.':
            count_points += 1
    return count_points < 2


def check_vaild_chars(equation: str) -> bool:
    """
    this method check all the characters in the equation is valid
    :param equation: the equation in str type
    :return: True if the all the characters in the equation is valid, False otherwise
    """
    for char in equation:
        if char not in VALID_CHARACTERS:
            return False
    return True


def is_integer(operand: str) -> bool:
    """
    this method check if the operand is integer
    :param operand: the operand in str type
    :return: True if the operand is integer, False otherwise
    """
    for i in range(len(operand)):
        if operand[i] == '.':
            if operand[i + 1] == '0':
                return True
            return False
    return True


def check_brackets_validation(equation: list, index: int) -> bool:
    """
    this method checks if the bracket is valid
    :param equation: the equation in list type
    :param index: the index in the list of the bracket
    :return: True if the bracket is valid, otherwise raise BracketsError
    """
    # if the amount of the brackets is not valid, raise BracketsError
    if not check_brackets_amount_validation(equation):
        raise BracketsError()
    if equation[index] == '(':
        # if from the left to the ( there is not an operator, raise BracketsError, else the bracket is valid
        if equation[index - 1] not in OPERATORS_LIST:
            raise BracketsError()
        else:
            return True
    # if the equation[index] is ')'
    else:
        # if from the left to the ( there is not an operator, raise BracketsError, else the bracket is valid
        if equation[index + 1] not in OPERATORS_LIST:
            raise BracketsError()
        else:
            return True


def check_brackets_amount_validation(equation: list) -> bool:
    """
    This method checks the validation of the brackets in the equation.
    :param: equation: the equation in list type
    :return: True if the brackets are valid, False otherwise.
    """
    brackets_stack = []
    # for each bracket in the equation
    for char in equation:
        # if the char is an opener, add it to the stack
        if char == '(':
            brackets_stack.append(OPENER_BRACKET)
        elif char == ')':
            # if the char is a closer, check if the stack is empty
            if len(brackets_stack) == 0:
                raise BracketsError()
            else:
                brackets_stack.pop()

    return len(brackets_stck) == 0


def is_unary_minus(equation: str, first_minus_index: int) -> int:
    if first_minus_index == 0:
        return True
    if 0 < first_minus_index < (len(equation) - 1):
        if is_number(equation[first_minus_index - 1]):
            return False
    else:
        raise MinusError
    return True


def is_number(char: str) -> bool:
    """
    the method check if a string can be a number (float number) or not
    :param char: string
    :return: True if a string can be a number and False if not
    """
    return char.isdigit() or char == '.' or is_float_number(char)


def is_char_in_number(char: str) -> bool:
    return char.isdigit() or char == '.' or char == '-'


def has_between_two_key(char: str) -> bool:
    """
    this method checks if the char is in BETWEEN_TWO_OPERATORS dict
    :param char: char in str type
    :return: the method returns True if the operator is in BETWEEN_TWO_OPERATORS dict, otherwise False
    """
    for key in BETWEEN_TWO_OPERATORS.keys():
        if char == key:
            return True
    return False


def has_between_one_key(char: str) -> (bool, str):
    """
    this method checks if the char is in BETWEEN_ONE_OPERATORS dict
    :param char: char in str type
    :return: 'right' if the operator is need to be from right to operand and 'left' if ot should be fro his right,
             in addition, the method returns True if the operator is in BETWEEN_ONE_OPERATORS dict, otherwise False
    """
    for key in BETWEEN_ONE_OPERATORS.keys():
        if char == key:
            if char == '!':
                side = "right"
            else:
                side = "left"
            return True, side
    return False, None


def is_float_number(operand: str) -> bool:
    """
    this method checks if a number is a float number
    :param operand: the equation in str type
    :return: the index of the last number of the calculation in the equation
    """
    index = 0
    for char in operand:
        if char == '.':
            if 0 < index < len(operand) - 1 and operand[index - 1].isdigit() and \
                    operand[index + 1].isdigit() and check_decimal_point_validate(operand):
                return True
            return False
        index += 1
    return False


# def check_equation_validation(equation_list: list):
#     index = 0
#     for item in equation_list:
#         if item in OPERATORS_LIST:
#             operator = get_operator()


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
    elif operator == '#':
        operator = Sum(equation, index)
    return operator
