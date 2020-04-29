import os

# Dictionaries directories.
DICTS = {
    "SPN": os.path.join(os.path.dirname(__file__), './dicts/spanish.txt'),
    "ENG": os.path.join(os.path.dirname(__file__), './dicts/english.txt')
}
DICTS_OPTIONS = {
    "SPN": ["SPN"],
    "ENG": ["ENG"],
    "ALL": list(DICTS.keys())
}


# Default representation of an unknown character.
DEFAULT_CHR = '*'
DEFAULT = -1

# Values used to identify spaces
SPACE = 32
IS_SPACE = 65

# Values used to validate results
MAX_VALUE = 122
UPPER_RNG = range(65, 91)
VALID_RNG = list(range(97, 123)) + [SPACE]
