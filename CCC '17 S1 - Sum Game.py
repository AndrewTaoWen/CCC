a = int(input())

b = 0

c = 0

d = input().split(' ')
e = input().split(' ')

f = -1

for i in range(a):
  b += int(d[i])
  c += int(e[i])
  if b == c:
    if i > f:
      f = i

print(f+1)