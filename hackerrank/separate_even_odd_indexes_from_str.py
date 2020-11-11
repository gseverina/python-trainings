def separate(line):
    a = line[0::2]
    b = line[1::2]
    return a + ' ' + b


if __name__ == "__main__":
    assert(separate("Hacker")) == "Hce akr"
    assert (separate("Rank")) == "Rn ak"
