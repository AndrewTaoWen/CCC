n = int(input())
t = []
p = []
m1 = {}

for _ in range(n):
    a, b = input().split(' ')
    m1[int(a)] = int(b)

keys = sorted(m1)

h = 0
j = 0

for i in range(len(keys) - 1):
    f = (keys[i + 1]) - (keys[i])
    g = m1.get(keys[i + 1]) - m1.get(keys[i])
    j = abs(g / f)
    if j > h:
        h = j

print(h)