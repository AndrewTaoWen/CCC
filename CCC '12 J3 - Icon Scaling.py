a = int(input())
b = ''

for i in range(a):
  print((a * '*') + (a * 'x') + (a * '*'))

for i in range(a):
  print((a * ' ') + (2 * a * 'x'))

for i in range(a):
  print((a * '*') + (a * ' ') + (a * '*'))
