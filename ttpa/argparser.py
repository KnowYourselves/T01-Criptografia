import argparse
import os


def file_in(file_path):
    """Parse input file."""
    err = f"The file \"{file_path}\" doesn't exist."
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(err)
    return file_path


def file_out(file_path):
    """Parse output file."""
    err = f"The file \"{file_path}\" already exists."
    if os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(err)
    return file_path


def parse():
    """Parse commandline arguments."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "input",
        help="Input file from which to read the cipher texts.",
        type=file_in
    )

    parser.add_argument(
        "-o",
        "--out",
        help="Output file to which to write the cipher texts.",
        type=file_out
    )

    parser.add_argument(
        "-d",
        "--dict",
        help="Dictonaries to use.",
        type=str,
        default='ALL',
        choices=['ENG', 'SPN', 'ALL']
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="increase output verbosity"
    )

    return parser.parse_args()
