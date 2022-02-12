a = int(input())

f = []
h = []

l_s1 = 0
l_s2 = 0
l_str1 = ''
l_str2 = ''

for i in range(a):
    b, c, d, e = input().split(' ')
    s = (2 * int(c) + 3 * int(d) + int(e))
    f.append(s)
    h.append(b)
    if s > l_s1:
        l_s1 = s
        l_str1 = b
    elif s == l_s1:
        if l_str1 > b:
            l_str1 = b

if f:
    f.remove(l_s1)
    h.remove(l_str1)

    # print(f, h)

    for i in range(a - 1):
        if f[i] > l_s2:
            l_s2 = f[i]
            l_str2 = h[i]
        elif f[i] == l_s2:
            if l_str2 > h[i]:
                l_str2 = h[i]

    print(l_str1)
    print(l_str2)
else:
    print('')
