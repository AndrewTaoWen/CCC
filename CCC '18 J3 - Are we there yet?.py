l = [int(i) for i in input().split()]

for i in range(len(l)+1):
    l2 = l.copy()
    l2.insert(i,0)

    curSum = 0
    for k in range(i,len(l2)):
        curSum += l2[k]
        l2[k] = curSum

    curSum2 = 0
    for j in range(i,-1,-1):
        # print(j, l2[j])
        # print(curSum2)
        curSum2 += l2[j]
        l2[j] = curSum2
    # l2[0] = curSum

    for i in l2:
        print(i, end = ' ')
    print()