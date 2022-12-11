from const import *


__all__ = [
    'welcome_output',
    'result_output',
    'end_of_calculation',
    'goodbye_output'
]


def welcome_output() -> str:
    """
    this method is the welcome string that showed for the user
    :return: the string that gets from the user
    """
    return input(f"\nHello, I'm OMEGA calculator :) \n"
                 f"type an equation and I will solve it for you \n"
                 f"you can use those operators: {list(OPERATORS_PRIORITY.keys())} \n"
                 f"enter the equation here: ")


def result_output(result: int):
    """
    this method is the result string that showed to the user after calculating his equation
    :return: the result of the calculation
    """
    print(f"\nthe result of your equation is: {result}")


def end_of_calculation() -> str:
    return input("type 'quit' to end calculating or anything else to calculating again :) ")


def goodbye_output():
    """
    this method prints to the user the
    """
    print("thank you for using OMEGA calculator!")

# def start_over_output():
#     """
#     this method prints to the user if he want to calculate another equation
#     :return: the string that gets from the user
#     """
#     return input(f"do you want to calculate an equation again?")
