string = list(input())

s = 0

Base = 0

d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

m = len(string)-1

for i in range(1, len(string), 2):

    pre = int(string[i-1])

    num = d[string[i]] * pre

    # print(i)
    if i < m:
        Base = d[string[i]]

        nextBase = d[string[i+2]]

        if Base < nextBase:
            s -= num
        else:
            s += num
    else:
        s += num


print(s)