from calculation import *


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
        super().__init__(equation, index)
        self.operator = '+'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 plus operand2 by using the relevant function
        :return: the result of the calculation
        """
        return plus_calculate(self.equation, self.index)


class Minus(Operator):
    """
    this class presents the Minus class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '-'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 minus operand2 by using the relevant function
        :return: the result of the calculation
        """
        return minus_calculate(self.equation, self.index)


class Multiply(Operator):
    """
    this class presents the Multiply class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '*'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 Multiply operand2 by using the relevant function
        :return: the result of the calculation
        """
        return mul_calculate(self.equation, self.index)


class Divide(Operator):
    """
    this class presents the Divide class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '/'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 divide operand2 by using the relevant function
        :return: the result of the calculation
        """
        return div_calculate(self.equation, self.index)


class Power(Operator):
    """
    this class presents the Power class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '^'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 Power operand2 by using the relevant function
        :return: the result of the calculation
        """
        return pow_calculate(self.equation, self.index)


class Modulo(Operator):
    """
    this class presents the Modulo class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '%'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates operand1 Modulo operand2 by using the relevant function
        :return: the result of the calculation
        """
        return mod_calculate(self.equation, self.index)


class Maximum(Operator):
    """
    this class presents the Maximum class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '$'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Maximum from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return max_calculate(self.equation, self.index)


class Minimum(Operator):
    """
    this class presents the Minimum class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '&'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Minimum from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return min_calculate(self.equation, self.index)


class Average(Operator):
    """
    this class presents the Average class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '@'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Average from operand1 and operand2 by using the relevant function
        :return: the result of the calculation
        """
        return avg_calculate(self.equation, self.index)


class Negative(Operator):
    """
    this class presents the Negative class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '~'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Negative of operand by using the relevant function
        :return: the result of the calculation
        """
        return neg_calculate(self.equation, self.index)


class Factorial(Operator):
    """
    this class presents the Factorial class
    """

    def __init__(self, equation: str, index: int):
        super().__init__(equation, index)
        self.operator = '!'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Factorial of operand by using the relevant function
        :return: the result of the calculation
        """
        return fac_calculate(self.equation, self.index)
