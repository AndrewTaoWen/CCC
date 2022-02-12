key = list(input())

bp = [i for i in input() if i not in ' !@#$%^&*,.:"/']

count = 0

message = []

m = ''

for i in bp:
    m += i
    if len(m) == len(key):
        message.append(list(m))
        m = ''

message.append(list(m))

d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13,
     'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

inv_d = {v: k for k, v in d.items()}

string = ''

for i in message:
    for j in range(len(i)):
        a = i[j].lower()
        b = key[j].lower()
        if a != 0:
            c = d[a] + d[b]
            # print(a,b,c)
            if c >= 26:
                c -= 26
            # if i[j] != key[j]:
            i[j] = inv_d[c].upper()

    string += ''.join(i)

print(string)