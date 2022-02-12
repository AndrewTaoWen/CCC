a = int(input())
d = []
e = []

for _ in range(a):
  b, c = input().split(',')
  d.append(b)
  e.append(c)

minX = int(min(d)) -1
minY = int(min(e)) -1

maxX = int(max(d)) +1
maxY = int(max(e)) +1

print(str(minX) + ',' + str(minY))
print(str(maxX) + ',' + str(maxY))