a = int(input())

while True:

    a += 1
    c = set()

    for i in str(a):
        if i in c:
            break
        else:
            c.add(i)
    else:
        print(a)
        break
