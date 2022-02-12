a = int(input())
b = input().split(' ')
c = input().split(' ')
d = {}

for i in range(a):
  d[b[i]] = c[i]
  if b[i] == c[i]:
    print('bad')
    break
else:
  dFlipped = {value:key for key, value in d.items()}
  if d == dFlipped:
    print('good')
  else:
    print('bad')