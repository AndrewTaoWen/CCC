l = []
l.append(int(input()))
l.append(int(input()))

i = 1
while True:
    currentT = l[i - 1] - l[i]
    if currentT >= 0:
        l.append(currentT)
    else:
        break
    i += 1

print(len(l))
