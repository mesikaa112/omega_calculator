from substring_number import substring_number, is_number
from exception import *


def check_plus_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of plus sign
    :param equation: the equation in str type
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
        elif operand2 == 0:
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
        elif operand2 == 0:
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
        raise IndexError("the index is not valid")


def check_negative_validate(equation: str, index: int) -> bool:
    """
    this method check the validation of negative sign
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: True if the sigh is valid
    """
    if 0 <= index < (len(equation) - 1):
        operand = substring_number(equation, index)[1]
        if not is_number(operand):
            raise AverageError()
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
    if 0 <= index < (len(equation) - 1):
        operand = substring_number(equation, index)[1]
        if not is_number(operand):
            raise FactorialError()
        return True
    else:
        raise IndexError("the index is not valid")
