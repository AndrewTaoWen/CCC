d = {}

while True:
    a = input()
    b, c = a.split(' ')
    d[b] = c
    if b == 'Waterloo':
        break

e = 200
g = ''

for i in d:
    f = int(d.get(i))
    if f < e:
        e = f

for i in d:
    if int(d.get(i)) == e:
        print(i)
        break
