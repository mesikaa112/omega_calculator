__all__ = [
    'OPERATORS_PRIORITY',
    'BETWEEN_ONE_OPERATORS',
    'BETWEEN_TWO_OPERATORS',
    'VALID_CHARACTERS',
    'INVALID_CHARACTERS',
    'OPERATORS_LIST'
]

OPERATORS_PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5, '~': 6, '!': 6, '#': 6}
OPERATORS_LIST = {'+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', '(', ')'}
BETWEEN_TWO_OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '%': 4, '$': 5, '&': 5, '@': 5}
BETWEEN_ONE_OPERATORS = {'~': "left", '!': "right", '#': "right"}
VALID_CHARACTERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '!', '.', '@', '#', '$', '%', '^',
                    '&', '*', '(', ')', '~', ' '}
INVALID_CHARACTERS = {' ', '\t'}
