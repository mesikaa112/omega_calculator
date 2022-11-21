from Operator import operators


def welcome_output():
    """
    this method is the welcome string that showed for the user
    :return: the string that gets from the user
    """
    return input(f"Hello, I'm OMEGA calculator :) \n"
                 f"type an equation and I will solve it for you \n"
                 f"you can use those operators: {list(operators.keys())} \n"
                 f"enter the equation here : ")
