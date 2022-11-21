"""
Author: Yonatan Mesika
Date: 20.11.2022
module-info: this module contains the classes of the operators
"""

import math


class Operator:
    """
    this class is the base class of all the operators classes
    """

    def __init__(self):
        self.operator = None
        # self.priority = 0

    def calculate(self, operand1, operand2) -> int:
        """
        this method is the method that overrides in the operators classes
        :param operand1: first number
        :param operand2: second number
        :return: pass
        """
        return None

    def is_valid_operator(self):
        return None


class Plus(Operator):
    """
        this class presents the Plus class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '+'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 plus operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return operand1 + operand2


class Minus(Operator):
    """
    this class presents the Minus class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '-'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 minus operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return operand1 - operand2


class Multiply(Operator):
    """
    this class presents the Multiply class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '*'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 Multiply operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return operand1 * operand2


class Divide(Operator):
    """
    this class presents the Divide class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '/'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 divide operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        if operand2 == 0:
            raise ValueError("you cant divide by 0!")
        return operand1 / operand2


class Power(Operator):
    """
    this class presents the Power class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '^'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 Power operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return math.pow(operand1, operand2)


class Modulo(Operator):
    """
    this class presents the Modulo class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '%'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates operand1 Modulo operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return operand1 % operand2


class Maximum(Operator):
    """
    this class presents the Maximum class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '$'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates the Maximum from operand1 and operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        if operand1 == operand2:
            raise ValueError("the operands are equal, can't find Maximum!")
        return max(operand1, operand2)


class Minimum(Operator):
    """
    this class presents the Minimum class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '&'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates the Minimum from operand1 and operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        if operand1 == operand2:
            raise ValueError("the operands are equal, can't find Minimum!")
        return min(operand1, operand2)


class Average(Operator):
    """
    this class presents the Average class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '@'

    def calculate(self, operand1: int, operand2: int) -> int:
        """
        this method calculates the Average from operand1 and operand2
        :param operand1: first number
        :param operand2: second number
        :return: the result of the calculation
        """
        return (operand1 + operand2) / 2


class Negative(Operator):
    """
    this class presents the Negative class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '~'

    def calculate(self, operand: int) -> int:
        """
        this method calculates the Negative of operand
        :param operand: number
        :return: the result of the calculation
        """
        return -operand


class Factorial(Operator):
    """
    this class presents the Factorial class
    """

    def __init__(self):
        super().__init__(self)
        self.operator = '!'

    def factorial_calc(self, operand: int) -> int:
        """
        this method is a recursive method that calculate the factorial of a number
        :param operand: number
        :return: the result of the calculation
        """
        if operand == 1:
            return 1
        return operand * factorial_calc(operand - 1)

    def calculate(self, operand: int) -> int:
        """
        this method calculates the Factorial of operand
        :param operand1: number
        :return: the result of the calculation
        """
        if not is_integer(operand):  ########################################################
            raise TypeError("Factorial must be done on an integer number!")
        if operand < 0:
            raise ValueError("Factorial can't be done on a negative number!")
        return factorial_calc(operand1)
