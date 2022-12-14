# from substring_number import substring_number, is_number, is_negative_number, substring_float_to_int
from exception import *
from const import *


def check_plus_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of plus sign
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 < index < (len(equation) - 1):
        operand1, operand2 = substring_number(equation, index)
        print(operand1, operand2)
        if (not is_number(operand1)) or (not is_number(operand2)):
            raise PlusError()
        return True
    else:
        raise IndexError("the index is not valid")


def check_unary_minus_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of unary minus sign
    :param equation: the equation in str type
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


def check_minus_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of minus sign
    :param equation: the equation in str type
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


def check_multiply_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of multiply sign
    :param equation: the equation in str type
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


def check_divide_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of divide sign
    :param equation: the equation in str type
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


def check_power_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of power sign
    :param equation: the equation in str type
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


def check_modulo_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of modulo sign
    :param equation: the equation in str type
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


def check_maximum_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of maximum sign
    :param equation: the equation in str type
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


def check_minimum_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of minimum sign
    :param equation: the equation in str type
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


def check_average_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of average sign
    :param equation: the equation in str type
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


def check_negative_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of negative sign
    :param equation: the equation in str type
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


def check_factorial_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of factorial sign
    :param equation: the equation in str type
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


def check_brackets_validation(equation: str) -> bool:
    """
    This method checks the validation of the brackets in the equation.
    :param: equation: the equation.
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


def is_number(operand: str) -> bool:
    """
    the method check if a string can be a number (float number) or not
    :param operand: string
    :return: True if a string can be a number and False if not
    """
    return operand.isdigit() or is_float_number(operand, operand.find('.')) or operand[1:].isdigit()



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


def is_float_number(equation: str, index: int) -> bool:
    """
    this method checks if a number
    :param equation: the equation in str type
    :param index: the index of the operator that used for calculate the specified calculation
    :return: the index of the last number of the calculation in the equation
    """
    if 0 < index < (len(equation) - 1) and equation[index] == '.':
        return equation[index - 1].isdigit() and equation[index + 1].isdigit()
    return False