a = input()
b = input()
c = []
d = 0

for i in range(len(b)):
  c.append(b)
  e = b[1:] + b[0]
  b = e

for i in c:
  d = a.find(i)
  if d != -1:
    print('yes')
    break
else:
  print('no')