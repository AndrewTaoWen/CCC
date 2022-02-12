a = input()
b = input()
c = input()
d = input()
e = []
f = []
g = []
h = []
t = 0

for i in a.split(' '):
    e.append(int(i))

for i in b.split(' '):
    f.append(int(i))

for i in c.split(' '):
    g.append(int(i))

for i in d.split(' '):
    h.append(int(i))

for i in range(4):
    j = int(e[i] + f[i] + g[i] + h[i])
    if (j == sum(e) == sum(f) == sum(g) == sum(h)):
        t += 1

if t == 4:
    print('magic')
else:
    print('not magic')
