a = int(input())
b = list(input())
c = list(input())

count = 0

for i in range(a):
    if b[i] == 'C' and c[i] == 'C':
        count += 1

print(count)