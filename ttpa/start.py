from .file_manager import read_file, write_answer
from .decipher import decipher
from .argparser import parse


def start():
    """Start program."""
    # Parse arguments
    args = parse()

    # Get the input codes
    codes, common_length, codes_length = read_file(args.input, args.verbose)

    # Get partial answer
    answer = decipher(codes, common_length, codes_length, args)

    # Write final answer
    if args.out:
        write_answer(answer, args.out, args.verbose)
