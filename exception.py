class Error(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PlusError(Error):
    def __init__(self, message="\nthere is an ERROR! the plus sign is the cause"):
        self.message = message
        super().__init__(self.message)


class MinusError(Error):
    def __init__(self, message="\nthere is an ERROR! the minus sign is the cause"):
        self.message = message
        super().__init__(self.message)


class MultiplyError(Error):
    def __init__(self, message="\nthere is an ERROR! the multiply sign is the cause"):
        self.message = message
        super().__init__(self.message)


class DivideError(Error):
    def __init__(self, message="\nthere is an ERROR! the divide sign is the cause"):
        self.message = message
        super().__init__(self.message)


class PowerError(Error):
    def __init__(self, message="\nthere is an ERROR! the power sign is the cause"):
        self.message = message
        super().__init__(self.message)


class ModuloError(Error):
    def __init__(self, message="\nthere is an ERROR! the modulo sign is the cause"):
        self.message = message
        super().__init__(self.message)


class MaximumError(Error):
    def __init__(self, message="\nthere is an ERROR! the maximum sign is the cause"):
        self.message = message
        super().__init__(self.message)


class MinimumError(Error):
    def __init__(self, message="\nthere is an ERROR! the minimum sign is the cause"):
        self.message = message
        super().__init__(self.message)


class AverageError(Error):
    def __init__(self, message="\nthere is an ERROR! the average sign is the cause"):
        self.message = message
        super().__init__(self.message)


class NegativeError(Error):
    def __init__(self, message="\nthere is an ERROR! the tilde sign is the cause"):
        self.message = message
        super().__init__(self.message)


class FactorialError(Error):
    def __init__(self, message="\nthere is an ERROR! the factorial sign is the cause"):
        self.message = message
        super().__init__(self.message)


class SumError(Error):
    def __init__(self, message="\nthere is an ERROR! the sum sign is the cause"):
        self.message = message
        super().__init__(self.message)


class EmptyInputError(Error):
    def __init__(self, message="\nthere is an ERROR! you entered an empty equation"):
        self.message = message
        super().__init__(self.message)


class DecimalPointError(Error):
    def __init__(self, message="\nthere is an ERROR! there is too much decimal points in operand"):
        self.message = message
        super().__init__(self.message)


class InValidCharsError(Error):
    def __init__(self, message="\nthere is an ERROR! you entered invalid characters"):
        self.message = message
        super().__init__(self.message)


class BracketsError(Error):
    def __init__(self, message="\nthere is an ERROR! the brackets are the cause"):
        self.message = message
        super().__init__(self.message)


class MissingOperandError(Error):
    def __init__(self, message="\nthere is an ERROR! the equation missing operand"):
        self.message = message
        super().__init__(self.message)
