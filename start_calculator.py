from exception import *
from welcome_output import welcome_output
from substring_number import substring_spaces


def start_calculation():
    """
    this method starts the calculation process and takes care on the exceptions
    """
    try:
        equation = welcome_output()
        if equation == "":
            raise EmptyInputError
        equation = substring_spaces(equation)
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
    except EmptyInputError as error:
        print(error)
    except EOFError as error:
        print(error)
