q = int(input())
m1p = int(input())
m2p = int(input())
m3p = int(input())

d = 0

while q > 0:

    q -= 1

    d += 1

    # print(d)

    if d % 3 == 0:
        m3p += 1
        if (m3p % 10 == 0):
            q += 9

    elif d % 2 == 0:
        m2p += 1
        if (m2p % 100 == 0):
            q += 60

    else:
        m1p += 1
        if (m1p % 35 == 0):
            q += 30

print('Martha plays ' + str(d) + ' times before going broke.')