def capitalize(s):
    if len(s) < 1:
        return ""

    to_upper = True
    r = []
    for i in range(len(s)-1):
        if to_upper:
            r.append(s[i].upper())
            to_upper = False
        else:
            r.append(s[i])
            if s[i] == " " and s[i+1] != " ":
                to_upper = True
    if s[len(s) - 2] == " ":
        r.append(s[len(s) - 1].upper())
    else:
        r.append(s[len(s) - 1])
    return "".join(r)


if __name__ == '__main__':
    print(capitalize("hello  world"))
    print(capitalize("12abc"))
    print(capitalize(""))
    print(capitalize("hello   world  lol"))
    print(capitalize("132 456 Wq  m e"))
