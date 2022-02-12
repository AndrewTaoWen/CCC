d1 = int(input())
d2 = int(input())

count = 0

for i in range(1,d1+1):
    for k in range(1,d2+1):
        if i + k == 10:
            count += 1

if count != 1:
    print('There are', count, 'ways to get the sum 10.')
else:
    print('There is 1 way to get the sum 10.')
