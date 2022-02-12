a = int(input())
b = int(input())
c = []
d = 0
e = 0

for i in range(b):
  c.append(int(input()))

c = sorted(c)

while d < a:

  for i in range(b):
    d += int(c[i])
    e += 1
    if d == a:
      break
    elif d > a:
      e -= 1
      break

print(e)