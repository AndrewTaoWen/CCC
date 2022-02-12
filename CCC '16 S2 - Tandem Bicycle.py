a = int(input())
b = int(input())
e = input().split(' ')
f = input().split(' ')
c = []
d = []

for i in e:
  c.append(int(i))
for i in f:
  d.append(int(i))

g = 0

if a == 1:
  c = sorted(c)
  d = sorted(d)
  for i in range(b):
    if c[i] > d[i]:
      g += int(c[i])
    elif c[i] < d[i]:
      g += int(d[i])
    elif c[i] == d[i]:
      g += int(c[i])
elif a == 2:
  c = sorted(c)
  d = sorted(d , reverse = True)
  for i in range(b):
    if c[i] > d[i]:
      g += int(c[i])
    elif c[i] < d[i]:
      g += int(d[i])
    elif c[i] == d[i]:
      g += int(c[i])

print(g)