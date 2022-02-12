a = int(input())
b = int(input())
c = []

count = -1

for i in range(b):
  count += 1
  c.append(int(input()))
  if sum(c) > a:
    print(count)
    break
  if len(c) == 4:
    c.pop(0)
else:
  print(b)