a = input()
b = []
c = '1'
d = '2'
e = '3'
f = '4'

for i in a:
  b.append(i)

for i in b:
  if i == "V":
    c,d = d,c
    e,f = f,e
  else:
    c,e = e,c
    d,f = f,d

print(c,d)
print(e,f)
