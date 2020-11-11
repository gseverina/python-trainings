from string import ascii_lowercase

word_values = {}
i = 1
for letter in ascii_lowercase:
    word_values.update({letter: i})
    i += 1


def sum_words(word):
    s = 0
    for l in word:
        s += word_values[l]
    return s


def high(x):
    d = dict()
    for word in x.split():
        d.update({word: sum_words(word)})
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return s[0][0]


assert high('man i need a taxi up to ubud') == 'taxi'
assert high('what time are we climbing up the volcano') == 'volcano'
assert high('take me to semynak') == 'semynak'
