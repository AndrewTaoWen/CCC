s = input()

lCnt = s.count('L')
mCnt = s.count('M')
sCnt = s.count('S')

if mCnt == 0:

    diff = 0
    for i in range(lCnt):
        if s[i] != 'L':
            diff += 1
    print(diff)
else:
    s = list(s)
    M = []
    S = []
    L = []

    for i in range(lCnt, lCnt + mCnt):
        if s[i] == 'L':
            M.append(i)

    for i in range(lCnt + mCnt, len(s)):
        if s[i] == 'L':
            S.append(i)
    # print(M)
    # print(S)
    cnt = 0
    for i in range(lCnt):
        if s[i] == 'S':
            if S:
                index = S.pop()
                s[index], s[i] = s[i], s[index]
                cnt += 1
            elif M:
                index = M.pop()
                s[index], s[i] = s[i], s[index]
                cnt += 1
        elif s[i] == 'M':
            if M:
                index = M.pop()
                s[index], s[i] = s[i], s[index]
                cnt += 1
            elif S:
                index = S.pop()
                s[index], s[i] = s[i], s[index]
                cnt += 1
        # print(s)
    # print(s)

    sortedS = sorted(s)
    diff = 0
    for i in range(lCnt, len(s)):
        if s[i] != sortedS[i]:
            diff += 1
    cnt += diff // 2
    print(cnt)