import math
from Validation import *

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}


class Operator:
    """
    this class is the base class of all the operators classes
    """

    def __init__(self, equation: str, index: int):
        self.operator = None
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method is the method that overrides in the operators classes
        :return: None
        """
        return None


class Plus(Operator):
    """
        this class presents the Plus class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '+'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 plus operand2
        :return: the result of the calculation
        """
        if check_plus_validate(self.equation, self.index):
            return operand1 + operand2
            # need to add function that return the number before and after the index


class Minus(Operator):
    """
    this class presents the Minus class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '-'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 minus operand2
        :return: the result of the calculation
        """
        if check_minus_validate(self.equation, self.index):
            return operand1 - operand2


class Multiply(Operator):
    """
    this class presents the Multiply class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '*'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 Multiply operand2
        :return: the result of the calculation
        """
        if check_multiply_validate(self.equation, self.index):
            return operand1 * operand2


class Divide(Operator):
    """
    this class presents the Divide class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '/'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 divide operand2
        :return: the result of the calculation
        """
        # if operand2 == 0:
        #     raise ValueError("you cant divide by 0!")
        if check_divide_validate(self.equation, self.index):
            return operand1 / operand2


class Power(Operator):
    """
    this class presents the Power class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '^'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 Power operand2
        :return: the result of the calculation
        """
        if check_power_validate(self.equation, self.index):
            return math.pow(operand1, operand2)


class Modulo(Operator):
    """
    this class presents the Modulo class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '%'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates operand1 Modulo operand2
        :return: the result of the calculation
        """
        if check_modulo_validate(self.equation, self.index):
            return operand1 % operand2


class Maximum(Operator):
    """
    this class presents the Maximum class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '$'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates the Maximum from operand1 and operand2
        :return: the result of the calculation
        """
        # if operand1 == operand2:
        #     raise ValueError("the operands are equal, can't find Maximum!")
        if check_maximum_validate(self.equation, self.index):
            return max(operand1, operand2)


class Minimum(Operator):
    """
    this class presents the Minimum class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '&'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates the Minimum from operand1 and operand2
        :return: the result of the calculation
        """
        # if operand1 == operand2:
        #     raise ValueError("the operands are equal, can't find Minimum!")
        if check_minimum_validate(self.equation, self.index):
            return min(operand1, operand2)


class Average(Operator):
    """
    this class presents the Average class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '@'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates the Average from operand1 and operand2
        :return: the result of the calculation
        """
        if check_average_validate(self.equation, self.index):
            return (operand1 + operand2) / 2


class Negative(Operator):
    """
    this class presents the Negative class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '~'
        self.equation = equation
        self.index = index

    def calculate(self) -> int:
        """
        this method calculates the Negative of operand
        :return: the result of the calculation
        """
        if check_negative_validate(self.equation, self.index):
            return -operand


class Factorial(Operator):
    """
    this class presents the Factorial class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(self)
        self.operator = '!'
        self.equation = equation
        self.index = index

    def factorial_calc(self, operand: int) -> int:
        """
        this method is a recursive method that calculate the factorial of a number
        :return: the result of the calculation
        """
        if operand == 1:
            return 1
        return operand * factorial_calc(operand - 1)

    def calculate(self) -> int:
        """
        this method calculates the Factorial of operand
        :return: the result of the calculation
        """
        # if not is_integer(operand):
        #     raise TypeError("Factorial must be done on an integer number!")
        # if operand < 0:
        #     raise ValueError("Factorial can't be done on a negative number!")
        if check_factorial_validate(self.equation, self.index):
            return factorial_calc(operand1)
