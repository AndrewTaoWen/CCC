N = int(input())
boards = [int(i) for i in input().split()]
d = [0 for _ in range(2001)]
for i in boards:
    d[i] += 1
# print(d)
lengths = [0 for _ in range(4001)]

for i in range(2001):
    for j in range(i, 2001):
        if i == j:
            s = i + j
            lengths[s] += d[i] // 2
        else:
            s = i + j
            lengths[s] += min(d[i], d[j])

m = max(lengths)
cnt = 0
for i in lengths:
    if i == m:
        cnt += 1

print(m, cnt)