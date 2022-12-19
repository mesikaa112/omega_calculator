from get_operator import *
from exception import *
from substring_number import *
from const import *


def check_plus_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of plus sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise PlusError()
    return True


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


def check_minus_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of minus sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand2)) and operand2 != '(':
        raise MinusError()
    return True


def check_multiply_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of multiply sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sign is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise MultiplyError()
    return True


def check_divide_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of divide sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise DivideError()
    elif operand2 == '0' or operand2 == '0.0':
        raise DivideError("There is an ERROR! you can't divide by zero")
    return True


def check_power_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of power sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise PowerError()
    if (operand1 == '0' or operand1 == '0.0') and (operand2 == '0' or operand2 == '0.0'):
        raise PowerError("there is an ERROR! you can't power 0 by 0")
    return True


def check_modulo_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of modulo sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise ModuloError()
    elif operand2 == '0' or operand2 == '0.0':
        raise ModuloError("There is an ERROR! you can't divide by zero")
    return True


def check_maximum_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of maximum sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sigh is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise MaximumError()
    return True


def check_minimum_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of minimum sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sign is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise MinimumError()
    return True


def check_average_validate(operand1: str, operand2: str) -> bool:
    """
    this method check the validation of average sign
    :param operand1: the operand from the left to the operator in str type
    :param operand2: the operand from the right to the operator in str type
    :return: True if the sign is valid
    """
    if (not is_number(operand1) and operand1 != ')') or (not is_number(operand2) and operand2 != '('):
        raise AverageError()
    return True


def check_negative_validation(equation: list):
    index = 0
    count_tilde = 0
    while index < len(equation):
        while index < len(equation) and ((not is_number(equation[index])) or equation[index] == '('):
            if equation[index] == '~':
                count_tilde += 1
            index += 1
        if count_tilde > 1:
            raise NegativeError()
        count_tilde = 0
        index += 1


def check_factorial_validate(operand: str) -> bool:
    """
    this method check the validation of factorial sign
    :param operand: the operand in str type
    :return: True if the sign is valid
    """
    if (is_number(operand) and is_negative_number(operand)) or not is_integer(operand):
        raise FactorialError()
    return True


def check_sum_validate(operand: str) -> bool:
    """
    this method check the validation of a sum sign
    :param operand: the operand in str type
    :return: True if the sigh is valid
    """
    if not is_number(operand) and operand != ')' or not is_integer(operand):
        raise SumError()
    return True


def check_vaild_chars(equation: list) -> bool:
    """
    this method check all the characters in the equation is valid
    :param equation: the equation in str type
    :return: True if the all the characters in the equation is valid, False otherwise
    """
    # on every item in the list
    for item in equation:
        # for every char in the item
        for char in item:
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
        if index > 0 and equation[index - 1] not in OPERATORS_LIST:
            raise BracketsError()
        else:
            return True
    # if the equation[index] is ')'
    else:
        # if from the left to the ( there is not an operator, raise BracketsError, else the bracket is valid
        if index < len(equation) - 1 and equation[index + 1] not in OPERATORS_LIST:
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
            brackets_stack.append(char)
        elif char == ')':
            # if the char is a closer, check if the stack is empty
            if len(brackets_stack) == 0:
                raise BracketsError()
            else:
                brackets_stack.pop()

    return len(brackets_stack) == 0


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


def check_between_two_operands_validation(operand1: str, operand2: str, operator: str):
    validation_func = get_between_two_operator_validation(operator)
    return validation_func(operand1, operand2)


def check_between_one_operands_validation(operand1: str, operand2: str, operator: str):
    validation_func = get_between_one_operator_validation(operator)
    if BETWEEN_ONE_OPERATORS.get(operator) == "left":
        return validation_func(operand2)
    else:
        return validation_func(operand1)


def check_equation_validation(equation_list: list):
    # if equation is empty
    if not equation_list:
        raise EmptyInputError()
    # if the equation contains invalid characters
    if not check_vaild_chars(equation_list):
        raise InValidCharsError()
