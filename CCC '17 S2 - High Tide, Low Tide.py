a = int(input())
b = input().split(' ')
lowT = []
highT = []
output = ''

b = sorted([int(b) for b in b])

if a % 2 != 0:
  for i in range(int(a/2)+1):
    lowT.append(b[i])
  for i in range(int(a/2)+1, a):
    highT.append(b[i])
else:
  for i in range(int(a/2)):
    lowT.append(b[i])
  for i in range(int(a/2), a):
    highT.append(b[i])

lowT = sorted(lowT, reverse = True)

c = -1
d = -1


for i in range(1, a+1):
  if i % 2 == 0:
    d += 1
    output += (str(highT[d]) + ' ')
  else:
    c += 1
    output += (str(lowT[c]) + ' ')

print(output)