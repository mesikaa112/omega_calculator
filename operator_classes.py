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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method is the method that overrides in the operators classes
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True
        """
        return True


class Plus(Operator):
    """
        this class presents the Plus class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the plus sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the plus sign is validate, False otherwise
        """
        return check_plus_validate(equation_list, index)


class Minus(Operator):
    """
    this class presents the Minus class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the minus sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the minus sign is validate, False otherwise
        """
        return check_minus_validate(equation_list, index)


class Multiply(Operator):
    """
    this class presents the Multiply class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the multiply sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the multiply sign is validate, False otherwise
        """
        return check_multiply_validate(equation_list, index)


class Divide(Operator):
    """
    this class presents the Divide class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the divide sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the divide sign is validate, False otherwise
        """
        return check_divide_validate(equation_list, index)


class Power(Operator):
    """
    this class presents the Power class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the power sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the power sign is validate, False otherwise
        """
        return check_power_validate(equation_list, index)


class Modulo(Operator):
    """
    this class presents the Modulo class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the modulo sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the modulo sign is validate, False otherwise
        """
        return check_modulo_validate(equation_list, index)


class Maximum(Operator):
    """
    this class presents the Maximum class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the maximum sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the maximum sign is validate, False otherwise
        """
        return check_maximum_validate(equation_list, index)


class Minimum(Operator):
    """
    this class presents the Minimum class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the minimum sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the minimum sign is validate, False otherwise
        """
        return check_minimum_validate(equation_list, index)


class Average(Operator):
    """
    this class presents the Average class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the average sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the average sign is validate, False otherwise
        """
        return check_average_validate(equation_list, index)


class Negative(Operator):
    """
    this class presents the Negative class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the negative sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the negative sign is validate, False otherwise
        """
        return check_negative_validate(equation_list, index)


class Factorial(Operator):
    """
    this class presents the Factorial class
    """

    def __init__(self, equation: list, index: int):
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

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the factorial sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the factorial sign is validate, False otherwise
        """
        return check_factorial_validate(equation_list, index)


class Sum(Operator):
    """
    this class presents the Sum class
    """

    def __init__(self, equation: list, index: int):
        super().__init__(equation, index)
        self.operator = '#'
        self.equation = equation
        self.index = index

    def calculate(self) -> float:
        """
        this method calculates the Sum of a few operands by using the relevant function
        :return: the result of the calculation
        """
        return sum_calculate(self.equation, self.index)

    def validation(self, equation_list: list, index: int) -> bool:
        """
        this method checks if the sum sign is validate by using the relevant operator
        :param equation_list: equation in list type
        :param index: the index of the operator
        :return: True if the sum sign is validate, False otherwise
        """
        return check_sum_validate(equation_list, index)
