a = int(input())

for _ in range(a):
  b = []
  c = int(input())
  for i in range(1, c):
    if c % i == 0:
      b.append(i)
  if sum(b) < c:
      print(str(c) + ' is a deficient number.')
  elif sum(b) == c:
      print(str(c) + ' is a perfect number.')
  else:
      print(str(c) + ' is an abundant number.')
