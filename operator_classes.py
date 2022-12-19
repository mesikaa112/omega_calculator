import validation
import calculation
from calculation import *


class Operator:
    """
    this class is the base class of all the operators classes
    """

    def __init__(self, equation: list, index: int):
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

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '+'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 plus operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.plus_calculate


class Minus(Operator):
    """
    this class presents the Minus class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '-'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 minus operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.minus_calculate


class Multiply(Operator):
    """
    this class presents the Multiply class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '*'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 Multiply operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.mul_calculate


class Divide(Operator):
    """
    this class presents the Divide class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '/'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 divide operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.div_calculate


class Power(Operator):
    """
    this class presents the Power class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '^'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 Power operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.pow_calculate


class Modulo(Operator):
    """
    this class presents the Modulo class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '%'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates operand1 Modulo operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.mod_calculate


class Maximum(Operator):
    """
    this class presents the Maximum class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '$'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Maximum from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.max_calculate


class Minimum(Operator):
    """
    this class presents the Minimum class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '&'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Minimum from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.min_calculate


class Average(Operator):
    """
    this class presents the Average class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '@'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Average from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return calculation.avg_calculate


class Negative(Operator):
    """
    this class presents the Negative class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '~'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Negative of operand by using the relevant function
        :return: the result of the calculation
        """
        return calculation.neg_calculate


class Factorial(Operator):
    """
    this class presents the Factorial class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '!'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Factorial of operand by using the relevant function
        :return: the result of the calculation
        """
        return calculation.fac_calculate


class Sum(Operator):
    """
    this class presents the Sum class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '#'
        self.equation = equation
        self.index = index

    def calculate(self):
        """
        this method calculates the Sum of a few operands by using the relevant function
        :return: the result of the calculation
        """
        return calculation.sum_calculate
