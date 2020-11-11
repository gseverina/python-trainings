# from Real Python - Medium Interview Question
key_map = {
    '*': '*',
    '**': '**',
    '***': '***',
    '#': '#',
    '##': '##',
    '###': '###',
    '1': '',
    '11': '',
    '111': '',
    '0': ' ',
    '2': 'a',
    '22': 'b',
    '222': 'c',
    '3': 'd',
    '33': 'e',
    '333': 'f',
    '4': 'g',
    '44': 'h',
    '444': 'i',
    '5': 'j',
    '55': 'k',
    '555': 'l',
    '6': 'm',
    '66': 'n',
    '666': 'o',
    '7': 'p',
    '77': 'q',
    '777': 'r',
    '7777': 's',
    '8': 't',
    '88': 'u',
    '888': 'v',
    '9': 'w',
    '99': 'x',
    '999': 'y',
    '9999': 'z',
}


def keypad_string(keys):
    """
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    """
    i = 0
    j = len(keys)
    if j == 0:
        return ""
    ret = ""
    while True:
        k = nk = nnk = nnnk = ''

        if i < j:
            k = keys[i]
        if i+1 < j:
            nk = keys[i+1]
        if i+2 < j:
            nnk = keys[i+2]
        if i+3 < j:
            nnnk = keys[i+3]

        if k != nk:
            ret += key_map[k]
            i += 1
        elif nk != nnk:
            s = f"{k}{nk}"
            ret += key_map[s]
            i += 2
        else:
            if nnnk == '7' or nnnk == '9':
                s = f"{k}{nk}{nnk}{nnnk}"
                i += 4
            else:
                s = f"{k}{nk}{nnk}"
                i += 3
            ret += key_map[s]
        if i >= len(keys):
            return ret

    return ret


if __name__ == "__main__":
    assert keypad_string("12345") == 'adgj'
    assert keypad_string("4433555555666") == 'hello'
    assert keypad_string("2022") == 'a b'
    assert keypad_string("") == ''
    assert keypad_string("111") == ''
    assert keypad_string("11") == ''
    assert keypad_string("1") == ''
    assert keypad_string("1111") == ''
    assert keypad_string("111111111111") == ''
