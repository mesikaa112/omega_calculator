from const import *
from validation import is_unary_minus, is_char_in_number, is_number
import re


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


def remove_duplicated_minuses(equation: str) -> str:
    """
    this method remove from a number his duplicated minuses
    :param equation: the number in str type
    :return: the operand with 1 or 0 minuses
    """
    last_minus_index = 0
    countNegatives = 0
    while last_minus_index < (len(equation) - 1):
        if equation[last_minus_index] == '-':
            first_minus_index = last_minus_index
            while last_minus_index < (len(equation) - 1) and equation[last_minus_index] == '-':
                last_minus_index += 1
                countNegatives += 1
            last_minus_index -= 1
            equation = replace_minuses(equation, first_minus_index, last_minus_index, countNegatives)
            last_minus_index = first_minus_index + 1
            countNegatives = 0
        else:
            last_minus_index += 1
    return equation


def replace_minuses(equation: str, first_minus_index: int, last_minus_index: int, countNegatives: int) -> str:
    if countNegatives % 2 == 0:
        # if is unary minus, delete all the minuses else replace all the minuses with plus sign
        if is_unary_minus(equation, first_minus_index): \
                return equation[:first_minus_index] + equation[last_minus_index + 1:]
        else:
            return equation[:first_minus_index] + '+' + equation[last_minus_index + 1:]
    # replace all the minuses with one minus
    else:
        return equation[:first_minus_index] + equation[last_minus_index:]


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
    operand1 = remove_duplicated_minuses(equation, operand1)
    buff = 1
    while (index + buff) < len(equation) and is_operator2_negative_number(equation, index, buff):
        operand2 += equation[index + buff]
        buff += 1
    while (index + buff) < len(equation) and (
            is_number(equation[index + buff]) or is_float_number(equation, (index + buff))):
        operand2 += equation[index + buff]
        buff += 1
    operand2 = remove_duplicated_minuses(equation, operand2)
    if if_only_negative_sign(operand2):
        operand2 = ''
    if if_only_negative_sign(operand1):
        operand1 = ''
    return operand1, operand2


def substring_invalid_characters(equation: str) -> str:
    """
    this method substring from the equation all the spaces
    :param equation: the equation in str type
    :return: the new str without the spaces
    """
    new_str = ""
    for char in equation:
        if char not in INVALID_CHARACTERS:
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
    while (index + buff) < len(equation) and (
            is_number(equation[index + buff]) or is_float_number(equation, (index + buff))):
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


def add_equation_to_list(equation: str) -> list:
    """
    this method add an equation into list in the same order
    :param equation: the equation in str type
    :return: the equation in str type
    """
    equation_list = []
    is_first_number = True
    for char in equation:
        # if the char is a number or '.'
        if is_number(char):
            # if this is the first char in the number
            if is_first_number:
                equation_list.append(char)
                is_first_number = False
            # if this is not first char in the number
            else:
                equation_list[-1] += char
        # if the char is an operator
        else:
            equation_list.append(char)
            is_first_number = True

    return equation_list


def infix_to_postfix(equation_list: list) -> list:
    """
    this method turns the equation list from infix to postfix
    :param equation_list: the equation in infix in list type
    :return: returns a list in of the equation in postfix
    """
    new_equation_list = []
    operators_stack = []
    for character in equation_list:
        # if character is number
        if is_number(character):
            new_equation_list.append(character)

        # else the character is an operator or ()
        else:
            if character == '(':
                operators_stack.append(character)

            elif character == ')':
                operator = operators_stack.pop()
                while operator != '(':
                    new_equation_list.append(operator)
                    operator = operators_stack.pop()

            # if the character is not ( or ) than the item must be an operator
            else:
                # appending the operators from the stack as long as they have a higher priority than the current
                # operator and the current top character is not ( and the stack isn't empty
                while len(operators_stack) > 0 and operators_stack[-1] != '(' \
                        and OPERATORS_PRIORITY[operators_stack[-1]] >= OPERATORS_PRIORITY[character]:
                    new_equation_list.append(operators_stack.pop())

                operators_stack.append(character)

    # at the end just append all of the remaining operators to the new list
    while len(operators_stack) > 0:
        new_equation_list.append(operators_stack.pop())

    return new_equation_list
