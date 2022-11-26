def is_number(operand: str) -> bool:
    """
        the method check if a string can be a number (float number) or not
        :param operand: string
        :return: True if a string can be a number and False if not
    """
    try:
        operand = float(operand)
        return True
    except ValueError:
        return False
    except EOFError:
        return False
    except Error:
        return False

#
# def check_plus_validate(equation: str, index: int) -> bool:
#     if
#
#     if index != 0 and is_number(str[index - 1]):
#         if str[index + 1] != '~' or str[index + 1] != '-':
#             if
#
#     return False
#
# def check_minus_validate(equation: str, index: int) -> bool:
# def check_multiply_validate(equation: str, index: int) -> bool:
# def check_divide_validate(equation: str, index: int) -> bool:
# def check_power_validate(equation: str, index: int) -> bool:
# def check_modulo_validate(equation: str, index: int) -> bool:
# def check_maximum_validate(equation: str, index: int) -> bool:
# def check_minimum_validate(equation: str, index: int) -> bool:
# def check_average_validate(equation: str, index: int) -> bool:
# def check_negative_validate(equation: str, index: int) -> bool:
# def check_factorial_validate(equation: str, index: int) -> bool:
