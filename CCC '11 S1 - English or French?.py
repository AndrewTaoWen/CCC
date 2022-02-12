a = int(input())
e = {}

for _ in range(a):
  b = input()
  # count and store in map
  for i in b:
    e[i] = e.get(i, 0) + 1

  # add number of each character
  c = e.get('t', 0) + e.get('T', 0)

  d = e.get('s', 0) + e.get('S', 0)

# determine language
if c > d:
  print('English')
else:
  print('French')