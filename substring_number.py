from const import *
from operator_classes import *


def remove_duplicated_minuses(equation: str) -> str:
    """
    this method remove from a number his duplicated minuses
    :param equation: the number in str type
    :return: the operand with 1 or 0 minuses
    """
    last_minus_index = 0
    count_negatives = 0
    while last_minus_index < (len(equation) - 1):
        if equation[last_minus_index] == '-':
            first_minus_index = last_minus_index
            while last_minus_index < (len(equation) - 1) and equation[last_minus_index] == '-':
                last_minus_index += 1
                count_negatives += 1
            last_minus_index -= 1
            equation = replace_minuses(equation, first_minus_index, last_minus_index, count_negatives)
            last_minus_index = first_minus_index + 1
            count_negatives = 0
        else:
            last_minus_index += 1
    return equation


def replace_minuses(equation: str, first_minus_index: int, last_minus_index: int, count_negatives: int) -> str:
    if count_negatives % 2 == 0:
        # if is unary minus, delete all the minuses else replace all the minuses with plus sign
        if is_unary_minus(equation, first_minus_index):
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
    for char in operand:
        if char == '-' and index == 0 and len(operand) > 1:
            return True
        index += 1
    return False


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


def substring_number(equation: list, index: int) -> (str, str):
    """
    this method substring from the equation the operands between the operator
    :param equation: the equation in list type
    :param index: the index in the equation of the operator
    :return: a tuple of two operands that were cut from the str
    """
    operand1 = ''   # the operand from the left to the operator
    operand2 = ''   # the operand from the right to the operator
    if 0 <= index < len(equation):
        if index > 0:
            # if operand1 is validate, if not so operand1 will be empty
            if is_number(equation[index - 1]) or equation[index - 1] == ')':
                operand1 = equation[index - 1]
        if index + 1 < len(equation):
            # if operand2 is validate, if not so operand2 will be empty
            if is_number(equation[index + 1]) or equation[index + 1] == '(':
                operand2 = equation[index + 1]
            # if operand2 is negative number
            elif (index + 2) < len(equation) and equation[index + 1] == '-' and (is_number(equation[index + 2]) or equation[index + 2] == '('):
                operand2 = equation[index + 1] + equation[index + 2]

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
    index = 0
    for char in equation:
        # if the char is a number or '.'
        if is_number(char) or (char == '-' and is_unary_minus(equation, index)):
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
        index += 1
    return equation_list


def infix_to_postfix(equation_list: list) -> list:
    """
    this method turns the equation list from infix to postfix
    :param equation_list: the equation in infix in list type
    :return: returns a list in of the equation in postfix
    """
    new_equation_list = []
    operators_stack = []
    index = 0
    # in case that there is - before brackets expression
    minus_stack = []
    for item in equation_list:
        # if item is number
        if is_number(item):
            new_equation_list.append(item)

        # else the item is an operator or ()
        else:
            # if there is a minus and the item after it is a '(' and the item before it is an operator, or the minuses
            # start the expression
            if item == '-' and equation_list[index + 1] == '(' and ((index - 1 < 0) or (index - 1 >= 0 and equation_list[index - 1] in OPERATORS_LIST)):
                # pushing 0 to later do 0 - expression
                new_equation_list.append('0')
                minus_stack.append(item)

            elif item == '(':
                operators_stack.append(item)
                # pushing '(' to the minus stack to know which of the () has a minus in front of it
                minus_stack.append(item)

            elif item == ')':
                operator = operators_stack.pop()
                while operator != '(':
                    new_equation_list.append(operator)
                    operator = operators_stack.pop()

                # popping out the '('
                minus_stack.pop()
                if len(minus_stack) > 0 and minus_stack[-1] == '-':
                    # adding to the new list the the minus that in the minus stack
                    new_equation_list.append(minus_stack.pop())

            # if the item is not ( or ) than the item must be an operator
            else:
                # appending the operators from the stack as long as they have a higher priority than the current
                # operator and the current top item is not ( and the stack isn't empty
                while len(operators_stack) > 0 and operators_stack[-1] != '(' \
                        and OPERATORS_PRIORITY[operators_stack[-1]] >= OPERATORS_PRIORITY[item]:
                    new_equation_list.append(operators_stack.pop())

                operators_stack.append(item)
        index += 1

    # at the end just append all of the remaining operators to the new list
    while len(operators_stack) > 0:
        new_equation_list.append(operators_stack.pop())

    return new_equation_list


def is_number(char: str) -> bool:
    """
    the method check if a string can be a number (float number) or not
    :param char: string
    :return: True if a string can be a number and False if not
    """
    return char.isdigit() or char == '.' or is_float_number(char) or is_negative_number(char)


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


def is_unary_minus(equation: str, first_minus_index: int) -> bool:
    if first_minus_index == 0:
        return True
    if 0 < first_minus_index < (len(equation) - 1):
        if is_number(equation[first_minus_index - 1]):
            return False
    else:
        raise MinusError
    return True
