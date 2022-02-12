a = input()
b = input()
c = input()
d = {}
e = []

for i in range(len(a)):
  d[a[i]] = b[i]

inv_d = {v: k for k, v in d.items()}

f = []


for i in inv_d.keys():
  f.append(i)

for i in c:
  if i in f:
    e.append(inv_d.get(i))
  else:
    e.append('.')


print(''.join(e))