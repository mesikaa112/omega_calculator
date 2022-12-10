def is_operator2_negative_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the right to the operator is negative number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking forward from the operator
    :return: True if the first char after the operator is '-' and False if not
    """
    return equation[index + buff] == '-' and buff == 1


def is_operator1_negative_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the left to the operator is negative number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking backward from the operator
    :return: True if first char after the operands is '-' and False if not
    """
    return equation[index - buff] == '-'


def is_operator2_float_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the left to the operator is a float number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking backward from the operator
    :return: True if there is a '.' in the number and False if not
    """
    if index - buff > 0:
        return equation[index - buff] == '.' and is_number(equation[index - buff - 1])


def is_operator1_float_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the right to the operator is a float number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking forward from the operator
    :return: True if there is a '.' in the number and False if not
    """
    if index + buff < len(equation) - 1:
        return equation[index + buff] == '.' and is_number(equation[index + buff + 1])


def if_only_negative_sign(operand: str) -> bool:
    """
    this method checks if the operand is only '-'
    :param operand: the number in str type
    :return: True if the number is only '-' and False if not
    """
    return operand == '-'


def is_negative_number(operand: str) -> bool:
    """
    this method checks if the operand negative or not
    :param operand: the number in str type
    :return: True if the number negative number or not
    """
    index = 0
    countNegatives = 0
    while index < (len(operand) - 1):
        if operand[index] == '-':
            countNegatives += 1
        index += 1
    if countNegatives % 2 == 0:
        return False
    return True


def remove_negative_sign(operand: str) -> str:
    """
    this method remove the negative signs from the number
    :param operand: the number in str type
    :return: the number without the negative signs in str type
    """
    index = len(operand) - 1
    if index == 0:
        return operand
    new_str = ""
    while operand[index] != '-':
        new_str = operand[index] + new_str
        index -= 1
    return new_str


def is_number(operand: str) -> bool:
    """
    the method check if a string can be a number (float number) or not
    :param operand: string
    :return: True if a string can be a number and False if not
    """
    try:
        abs_number = remove_negative_sign(operand)
        if is_negative_number(operand):
            abs_number = '-' + abs_number
        operand = abs_number
        float(operand)
        return True
    except ValueError:
        return False
    except EOFError:
        return False
    except Exception:
        return False


def substring_number(equation: str, index: int) -> (str, str):
    """
    this method substring from the equation the operands between the operator
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :return: a tuple of two operands that were cut from the str
    """
    operand1 = ''
    operand2 = ''
    buff = 1
    while (index - buff) >= 0 and (
            is_number(equation[index - buff]) or is_operator1_negative_number(equation, index,
                                                                              buff) or is_operator1_float_number(
        equation, index, buff)):
        operand1 = equation[index - buff] + operand1
        buff += 1
    buff = 1
    while (index + buff) < len(equation) and (
            is_number(equation[index + buff]) or is_operator2_negative_number(equation, index,
                                                                              buff) or is_operator2_float_number(
        equation, index, buff)):
        operand2 += equation[index + buff]
        buff += 1
    if if_only_negative_sign(operand2):
        operand2 = ''
    return operand1, operand2


def substring_spaces(equation: str) -> str:
    """
    this method substring from the equation all the spaces
    :param equation: the equation in str type
    :return: the new str without the spaces
    """
    new_str = ""
    for char in equation:
        if not char.isspace():
            new_str = new_str + char
    return new_str