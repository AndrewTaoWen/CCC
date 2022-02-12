a = int(input())
b = []

for _ in range(a):
  c, d, e = input().split()
  if 2007 - int(c) == 18:
    if (2 - int(d) < 0):
      print('No')
    elif (2 - int(d) == 0) and (27 - int(e) >= 0):
      print('Yes')
    elif (2 - int(d) == 1):
      print('Yes')
    else:
      print('No')
  elif 2007 - int(c) > 18:
    print('Yes')
  elif 2007 - int(c) < 18:
    print('No')