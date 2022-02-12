a = int(input())
b = []
c = []
d = 0

for _ in range(a):
    b.append(input())

for _ in range(a):
    c.append(input())

for i in range(a):
    if b[i] == c[i]:
        d += 1

print(d)