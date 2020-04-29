from collections import defaultdict
from .utils import solve_column
from . import parameters as p


def solve_by_spaces(answer, xors,  common_length, codes_length):
    """Find spaces for each code in codes."""
    # For each phrase
    for phrase_index in range(codes_length):
        # For each character
        for word_index in range(common_length):
            # Try to find another phrase which xor value is less than 65
            other = None
            for key, _xor in xors.items():
                if phrase_index in key and 65 <= _xor[word_index] <= p.MAX_VALUE:
                    other = key[0] if key[0] != phrase_index else key[1]
                    break

            # For the found phrase try to find another one with xor < 32
            for key, _xor in xors.items():
                # If it is found,,then is a space
                if other in key and 0 < _xor[word_index] < 32:
                    # Use the space to solve its column
                    answer = solve_column(
                        xors, phrase_index, word_index, p.SPACE,
                        codes_length, answer
                    )
    return answer
