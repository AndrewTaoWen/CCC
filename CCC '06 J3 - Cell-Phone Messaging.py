d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 1, 'e': 2, 'f': 3}
d3 = {'g': 1, 'h': 2, 'i': 3}
d4 = {'j': 1, 'k': 2, 'l': 3}
d5 = {'m': 1, 'n': 2, 'o': 3}
d6 = {'p': 1, 'q': 2, 'r': 3, 's': 4}
d7 = {'t': 1, 'u': 2, 'v': 3}
d8 = {'w': 1, 'x': 2, 'y': 3, 'z': 4}

l = [d1, d2, d3, d4, d5, d6, d7, d8]

while True:
    string = input()
    if string == 'halt':
        break
    s = 0
    for i in range(0, len(string)):
        for j in l:
            if string[i] in j:
                s += j[string[i]]
                if i > 0:
                    if string[i - 1] in j:
                        s += 2

    print(s)