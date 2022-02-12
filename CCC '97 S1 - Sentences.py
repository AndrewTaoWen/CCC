num = int(input())

for i in range(num):
    a = int(input())
    b = int(input())
    c = int(input())

    L = []

    A = []
    for _ in range(a):
        A.append(input())

    B = []
    for _ in range(b):
        B.append(input())

    C = []
    for _ in range(c):
        C.append(input())

    for i in A:
        for j in B:
            for k in C:
                print(f'{i} {j} {k}.')
