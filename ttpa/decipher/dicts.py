import os
from .utils import solve_column, get_chr, get_str_answer
from . import parameters as p


def get_dict(name):
    """Read given dictonary."""
    with open(p.DICTS[name], 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def fits_word(word, guess):
    """See if a guess fits a word."""
    return all(
        word[i] == guess[i]
        for i in range(len(word))
        if word[i] != p.DEFAULT_CHR
    )


def find_match(phrase, word, guess, offset):
    """Find the indexes found by the guess."""
    word_index = phrase.index(word)
    found = [
        (index + word_index + offset, ord(guess[index]))
        for index in range(len(word))
        if word[index] == p.DEFAULT_CHR
    ]
    return found


def solve_by_dicts(answer, xors, codes_length, args):
    """Solve the cipher text by using the given dicts."""
    # For each dict
    dicts = p.DICTS_OPTIONS[args.dict]
    for dict_name in dicts:
        if args.verbose:
            print(f"Parsing the {dict_name} dictonary.")
        # For each phrase
        for phrase_index in range(codes_length):
            # Detect al the unsolved phrases
            phrase_ints = answer[phrase_index]
            offset = answer[phrase_index].count(0)
            phrase_str = "".join(map(get_chr, phrase_ints))
            all_words = filter(len, phrase_str.split(" "))
            not_solved = filter(lambda word: p.DEFAULT_CHR in word, all_words)

            # For each unsolved word
            for word in not_solved:
                # Read the dict
                dictonary = get_dict(dict_name)
                word_len = len(word)

                # And find all valid options
                options = filter(
                    lambda guess: len(guess) == word_len,
                    dictonary
                )
                valid = list(filter(
                    lambda guess: fits_word(word, guess),
                    options
                ))

                # If there's only one valid option
                if len(set(valid)) == 1:
                    guess = valid[0]
                    # Find the solved characters
                    match = find_match(phrase_str, word, guess, offset)

                    # Solve the columns of the found characters.
                    for word_index, valid_char in match:
                        answer = solve_column(
                            xors, phrase_index, word_index, valid_char,
                            codes_length, answer
                        )
        if args.verbose:
            print(f"Current Results:\n{get_str_answer(answer)}")

    return answer
