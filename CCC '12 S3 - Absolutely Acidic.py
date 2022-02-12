n = int(input())

d = {}

for i in range(n):
    num = int(input())
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

a = [int(i) for i in d.values()]

curL = max(a)

a = [i for i in a if i != curL]

if a:
    cur2ndL = max(a)

l = []

l2 = []

for i in d:
    if d[i] == curL:
        l.append(i)
    elif d[i] == cur2ndL:
        l2.append(i)

maxDiff = 0

if len(l) == 1:
    for i in l:
        for j in l2:
            curA = abs(i - j)
            if curA > maxDiff:
                maxDiff = curA
else:
    for i in l:
        for j in l:
            curA = abs(i - j)
            if curA > maxDiff:
                maxDiff = curA

print(maxDiff)
