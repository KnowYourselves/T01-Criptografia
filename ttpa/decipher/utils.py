from . import parameters as p
from itertools import product


def xor(x, y, length):
    """Perform x xor y."""
    return bytearray(x[i] ^ y[i] for i in range(length))


def get_xor(xors, i, j):
    """Get the xor between the code i and j."""
    default = bytearray()
    key = (i, j)
    result = xors.get(key, default) + xors.get(key[::-1], default)
    return result


def xor_product(codes, common_length, codes_length):
    """
    Calculate all the possible combination of xors betweem the given codes.

    Return
    ------
    A dict of bytearrays, where each key is a tuple in the form i, j and the
    corresponding value is codes[i] xor codes[j].

    """
    xors = dict()
    # For each possible combination, add the xor operation
    for i, j in product(range(codes_length), range(codes_length)):
        key = (i, j)
        # Since xor is commutative, just add pairs once
        if i != j and key not in xors and key[::-1] not in xors:
            code_i = codes[i]
            code_j = codes[j]
            xors[key] = xor(code_i, code_j, common_length)
    return xors


def trim_key(answer, codes, common_length, codes_length):
    """Detect and trim the key out of the cipher texts."""
    # For each cipher cod
    for phrase_index in range(codes_length):
        # And each of its characters
        for word_index in range(common_length):
            # If its value is within the valid range then the original
            # message didnt have a char in this index.
            if codes[phrase_index][word_index] in p.VALID_RNG:
                answer[phrase_index][word_index] = 0
    return answer


def solve_column(xors, phrase_index, word_index, valid_char, length, answer):
    """Solve a column of the cipher texts by using the given char."""
    FIX_SPACES = False

    answer[phrase_index][word_index] = valid_char
    for index in range(length):
        _xor = get_xor(xors, phrase_index, index)
        if _xor and answer[index][word_index]:
            result = _xor[word_index] ^ valid_char
            if not result:
                result = 0
            elif result in p.UPPER_RNG:
                FIX_SPACES = True
                result += p.SPACE
            answer[index][word_index] = result

    if FIX_SPACES:
        for index in range(length):
            value = answer[index][word_index]
            if value == p.SPACE:
                answer[index][word_index] = 0
    return answer


def get_str_answer(answer):
    """Get the answer in human readable format."""
    phrases = list(map(lambda row: ''.join(map(get_chr, row)), answer))
    return ('\t' + '\n\t'.join([
        f"({index + 1}) {phrases[index]}" for index in range(len(answer))
    ]))


def get_template(common_length, codes_length):
    """Create an answer template."""
    template = []
    for _ in range(codes_length):
        template.append([p.DEFAULT] * common_length)
    return template


def get_chr(char):
    """Get the string representation of a char."""
    if not char:
        return ''
    elif char == -1:
        return p.DEFAULT_CHR
    else:
        return chr(char)
