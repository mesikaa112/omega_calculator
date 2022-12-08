from operator import operators


def welcome_output() -> str:
    """
    this method is the welcome string that showed for the user
    :return: the string that gets from the user
    """
    return input(f"Hello, I'm OMEGA calculator :) \n"
                 f"type an equation and I will solve it for you \n"
                 f"you can use those operators: {list(operators.keys())} \n"
                 f"enter the equation here : ")

# def start_over_output():
#     """
#     this method prints to the user if he want to calculate another equation
#     :return: the string that gets from the user
#     """
#     return input(f"do you want to calculate an equation again?")
