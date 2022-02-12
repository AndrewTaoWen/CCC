a = int(input())

for i in range(a):
    b = input().split()
    for i in range(len(b)):
        if len(b[i]) == 4:
            b[i] = '****'
    print(' '.join(b))