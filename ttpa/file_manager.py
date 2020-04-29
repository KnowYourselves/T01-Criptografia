import sys
import os


def read_file(file_path, verbose):
    """Read the lines of the given file."""
    if verbose:
        print(f"Opening file {file_path}.")

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = map(str.strip, file.readlines())
        lines = list(map(bytes.fromhex, lines))

    if verbose:
        print(f"File opened successfully.")

    return lines, len(lines[0]), len(lines)


def write_answer(answer, file_path, verbose):
    """Write the answer to the given file."""
    if verbose:
        print(f"Writing answer on file.")

    answer = answer.replace('\t', '')
    answer = '\n'.join(map(
        lambda x: x[x.index(')') + 2:],
        answer.split("\n"))
    )
    with open(file_path, 'w') as file:
        file.write(f"{answer}\n")

    if verbose:
        print(f"File writen successfully.")
