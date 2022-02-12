a = int(input())
b = int(input())

if a % b == 0:
    print(a // b)
else:
    if a > b:
        c = a // b
        d = (a / b) - (a // b)
        e = 0
        f = 0
        term = False

        for i in range(1,a+1):
            for j in range(1,a+1):
                if round(i/j, 10) == round(d,10):
                    # print(i,j)
                    e = i
                    f = j
                    term = True
                    break

            if term == True:
                break

        print(c, f'{e}/{f}')
    else:
        # print('y')
        c = a / b
        term = False

        for i in range(1, b+1):
            for j in range(1, b+1):
                if round(i / j, 10) == round(c, 10):
                    term = True
                    print(f'{i}/{j}')
                    break
            if term == True:
                break