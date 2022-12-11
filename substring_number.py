from const import *


def is_operator2_negative_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the right to the operator is negative number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking forward from the operator
    :return: True if the first char after the operator is '-' and False if not
    """
    return equation[index + buff] == '-'


def is_operator1_negative_number(equation: str, index: int, buff: int) -> bool:
    """
    this method checks if the operand from the left to the operator is negative number
    :param equation: the equation in str type
    :param index: the index in the equation of the operator
    :param buff: the number of steps that taking backward from the operator
    :return: True if first char after the operands is '-' and False if not
    """
    return equation[index - buff] == '-'


def if_only_negative_sign(operand: str) -> bool:
    """
    this method checks if the operand is only '-'
    :param operand: the number in str type
    :return: True if the number is only '-' and False if not
    """
    return operand == '-'


def remove_duplicated_minuses(operand: str) -> str:
    """
    this method remove from a number his duplicated minuses
    :param operand: the number in str type
    :return: the operand with 1 or 0 minuses
    """
    index = 0
    countNegatives = 0
    while index < (len(operand) - 1):
        if operand[index] == '-':
            countNegatives += 1
        else:
            break
        index += 1
    if countNegatives == 0:
        return operand
    if countNegatives % 2 == 0:
        operand = operand[index:]
    else:
        operand = '-' + operand[index:]
    return operand


def is_negative_number(operand: str) -> bool:
    """
    this method checks if the operand is negative
    :param operand: the number in str type
    :return: True if the number is only '-' and False if not
    """
    index = 0
    countNegatives = 0
    while index < (len(operand) - 1):
        if operand[index] == '-':
            countNegatives += 1
        index += 1
    return not countNegatives % 2 == 0


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


def is_number(operand: str) -> bool:
    """
    the method check if a string can be a number (float number) or not
    :param operand: string
    :return: True if a string can be a number and False if not
    """
    return operand.isdigit() or is_float_number(operand, operand.find('.')) or operand[1:].isdigit()


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
    while (index - buff) >= 0 and (is_number(equation[index - buff]) or is_float_number(equation, (index - buff))):
        operand1 = equation[index - buff] + operand1
        buff += 1
    while (index - buff) >= 0 and is_operator1_negative_number(equation, index, buff):
        operand1 = equation[index - buff] + operand1
        buff += 1
    operand1 = remove_duplicated_minuses(operand1)
    buff = 1
    while (index + buff) < len(equation) and is_operator2_negative_number(equation, index, buff):
        operand2 += equation[index + buff]
        buff += 1
    while (index + buff) < len(equation) and (is_number(equation[index + buff]) or is_float_number(equation, (index + buff))):
        operand2 += equation[index + buff]
        buff += 1
    operand2 = remove_duplicated_minuses(operand2)
    if if_only_negative_sign(operand2):
        operand2 = ''
    if if_only_negative_sign(operand1):
        operand1 = ''
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


def get_index_for_operand1(equation: str, index: int) -> int:
    """
    this method find the index of the first number of the calculation in the equation
    :param equation: the equation in str type
    :param index: the index of the operator that used for calculate the specified calculation
    :return: the index of the first number of the calculation in the equation
    """
    index_of_operand1 = index
    buff = 1
    while (index - buff) >= 0 and (is_number(equation[index - buff]) or is_float_number(equation, (index - buff))):
        index_of_operand1 -= 1
        buff += 1
    while (index - buff) >= 0 and is_operator1_negative_number(equation, index, buff):
        index_of_operand1 -= 1
        buff += 1
    return index_of_operand1


def get_index_for_operand2(equation: str, index: int) -> int:
    """
    this method find the index of the last number of the calculation in the equation
    :param equation: the equation in str type
    :param index: the index of the operator that used for calculate the specified calculation
    :return: the index of the last number of the calculation in the equation
    """
    index_of_operand2 = index
    buff = 1
    while (index + buff) < len(equation) and is_operator2_negative_number(equation, index, buff):
        index_of_operand2 += 1
        buff += 1
    while (index + buff) < len(equation) and (is_number(equation[index + buff]) or is_float_number(equation, (index + buff))):
        index_of_operand2 += 1
        buff += 1
    return index_of_operand2


def add_result_to_equation(equation: str, result: float, index: int) -> str:
    """
    this method replace the specified calculation with the result of it in the equation
    :param equation: equation in str type
    :param result: a result of a calculation
    :param index: the index of the operator that used for calculate the specified calculation
    :return: the equation with the changes
    """
    if has_between_one_key(equation[index])[0]:
        side = has_between_one_key(equation[index])[1]
        if side == "left":
            index_end_of_operand2 = get_index_for_operand2(equation, index)
            index_beginning_of_operand1 = index
        elif side == "right":
            index_beginning_of_operand1 = get_index_for_operand1(equation, index)
            index_end_of_operand2 = index

    else:
        index_beginning_of_operand1 = get_index_for_operand1(equation, index)
        index_end_of_operand2 = get_index_for_operand2(equation, index)

    first_part_equation = equation[:index_beginning_of_operand1]
    second_part_equation = equation[index_end_of_operand2 + 1:]
    equation = first_part_equation + str(result) + second_part_equation

    return equation


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


def substring_float_to_int(operand: str) -> int:
    """
    this method substring a float number into int number
    :param operand: operand in str type
    :return: an int number
    """
    for i in range(len(operand)):
        if operand[i] == '.':
            return int(operand[: i])
    return int(operand)
