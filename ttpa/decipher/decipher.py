from .parameters import *
from .dicts import solve_by_dicts
from .spaces import solve_by_spaces
from .utils import solve_column, get_chr, get_template, trim_key, xor_product, get_str_answer
from itertools import product


def decipher(codes, common_length, codes_length, args):
    """Get all the recoverable information from the given cipher texts."""
    # Start answer template
    answer = get_template(common_length, codes_length)

    # Trim the key from the answer
    answer = trim_key(answer, codes, common_length, codes_length)

    if args.verbose:
        print("The key has been trimmed.")
        print(get_str_answer(answer))

    # Obtain possible xor combinations.
    xors = xor_product(codes, common_length, codes_length)

    # Find spaces with the given codes
    answer = solve_by_spaces(answer, xors, common_length, codes_length)

    if args.verbose:
        print("The spaces have been discovered and solved.")
        print(get_str_answer(answer))

    # Check the spanish dictonary for matches
    answer = solve_by_dicts(
        answer, xors, codes_length, args
    )

    if args.verbose:
        print("The analisys by dictonaries has finished.")

    # Get final string
    final = get_str_answer(answer)

    print(f"The final answer is:\n{final}")
    return final
