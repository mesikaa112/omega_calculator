from output import *
from calculation import *
from substring_number import *
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
        except SumError as error:
            print(error)
        except EmptyInputError as error:
            print(error)
        except IndexError as error:
            print(error)
        except DecimalPointError as error:
            print(error)
        except InValidCharsError as error:
            print(error)
        except ValueError as error:
            print(error)
        except EOFError as error:
            print(error)


def calculate(equation: str) -> float:
    """
    this method calculates the result of the equation
    :param equation: the equation in str type
    :return: the result of the final calculation in int type
    """
    equation = substring_invalid_characters(equation)
    equation = remove_duplicated_minuses(equation)
    equation_list = add_equation_to_list(equation)
    print(equation_list)
    check_equation_validation(equation_list)
    print(equation_list)
    equation_list = infix_to_postfix(equation_list)
    print(equation_list)
    return calculate_postfix(equation_list)


def calculate_postfix(equation: list) -> float:
    operands_stack = []
    operand1 = ""
    operand2 = ""
    for item in equation:
        # if the item is a number, push it to the stack
        if is_number(item):
            operands_stack.append(item)
        # the item is an operator
        else:
            # if the operator is an operator that should be between 2 operands
            if item in BETWEEN_TWO_OPERATORS:
                operand2 = operands_stack.pop()
                operand1 = operands_stack.pop()
                # check the validation of the operator
                check_between_two_operands_validation(operand1, operand2, item)
                # if the operator is valid, calculate
                operands_stack.append(str(calculate_sub_equation(operand1, item, operand2)))

            # if the operator is an operator that should be between 1 operand
            else:
                # if the operator should be from the left to the number
                if BETWEEN_ONE_OPERATORS.get(item) == "left":
                    operand2 = operands_stack.pop()
                    # check the validation of the operator
                    check_between_one_operands_validation(operand1, operand2, item)
                    # if the operator is valid, calculate
                    operands_stack.append(str(calculate_sub_equation(operand1, item, operand2)))
                # if the operator should be from the right to the number
                else:
                    operand1 = operands_stack.pop()
                    # check the validation of the operator
                    check_between_one_operands_validation(operand1, operand2, item)
                    # if the operator is valid, calculate
                    operands_stack.append(str(calculate_sub_equation(operand1, item, operand2)))
        operand1 = ""
        operand2 = ""
    return operands_stack.pop()
