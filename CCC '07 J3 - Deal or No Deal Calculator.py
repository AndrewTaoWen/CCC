num = int(input())
l = set()

for i in range(num):
    l.add(int(input()))

offer = int(input())

d = {1:100, 2:500, 3:1000, 4:5000, 5:10000, 6:25000, 7:50000, 8:100000, 9:500000, 10:1000000}

s = 0
cnt = 0

for i in d:
    if i in l:
        pass
    else:
        s += d[i]
        cnt += 1

average = s / cnt

if average > offer:
    print('no deal')
else:
    print('deal')