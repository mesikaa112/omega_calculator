__all__ = [
    'OPERATORS_PRIORITY',
    'BETWEEN_ONE_OPERATORS',
    'BETWEEN_TWO_OPERATORS',
    'VALID_CHARACTERS',
    'INVALID_CHARACTERS'
]

OPERATORS_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6}
BETWEEN_TWO_OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5}
BETWEEN_ONE_OPERATORS = {'~': 6, '!': 6}
VALID_CHARACTERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '!', '.', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', ' '}
INVALID_CHARACTERS = {' '}
