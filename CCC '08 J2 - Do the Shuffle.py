l = list('ABCDE')

while True:
    btn = int(input())
    clicks = int(input())

    if btn == 4 and clicks == 1:
        print(' '.join(l))
        break

    elif btn == 1:
        for i in range(clicks):
            l.append(l.pop(0))
    elif btn == 3:
        for i in range(clicks):
            l[0], l[1] = l[1], l[0]

    elif btn == 2:
        for i in range(clicks):
            l.insert(0, l.pop())
