a = int(input())
b = []
c = []

for _ in range(a):
  b.append(int(input()))

b = sorted(b)

for i in range(len(b)-1):
  c.append((b[i+1] - b[i])/2)

d = []

for j in range(len(c)-1):
    d.append(c[j+1]+c[j])

print(min(d))
