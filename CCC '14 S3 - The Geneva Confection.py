T = int(input())

for i in range(T):
    t = []
    branch = []
    car = 1
    n = int(input())
    for j in range(n):
        t.append(int(input()))
    while car <= n:
        if len(t) == 0 and branch[-1] != car:
            print('N')
            break
        if len(t) > 0 and t[-1] == car:
            t.pop()
            car += 1
        elif len(branch) > 0 and branch[-1] == car:
            branch.pop()
            car += 1
        else:
            branch.append(t.pop())
    else:
        print('Y')