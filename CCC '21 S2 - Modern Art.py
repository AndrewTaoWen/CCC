m = int(input())
n = int(input())
num = int(input())

brushH = set()
brushV = set()

for _ in range(num):
    l = input().split()
    # print(l)
    digit = int(l[1]) - 1
    if l[0] == 'C':
        if digit in brushV:
            brushV.remove(digit)
        else:
            brushV.add(digit)
    elif l[0] == 'R':
        if digit in brushH:
            brushH.remove(digit)
        else:
            brushH.add(digit)

canvas = [[0 for i in range(n)] for i in range(m)]

for i in brushH:
    canvas[i] = [1 for i in range(n)]

for i in range(m):
    for j in brushV:
        canvas[i][j] += 1

cnt = 0
for i in canvas:
    for j in i:
        if j % 2 != 0:
            cnt += 1

print(cnt)