n = int(input())

leftBound = {}
rightBound = {}

position = []
walk = []
dist = []

for i in range(n):
    p, w, d = map(int, input().split())
    position.append(p)
    walk.append(w)
    dist.append(d)

low = min(position)
high = max(position)

totalR = 0
totalL = 0

for i in range(n):
    r = position[i] + dist[i]
    if low <= r <= high:
        rightBound[r] = rightBound.get(r, 0) + walk[i]
        totalR += (high - r) * walk[i]
    l = position[i] - dist[i]
    if low <= l <= high:
        leftBound[l] = leftBound.get(l, 0) + walk[i]
        totalL += (l - low) * walk[i]

# print('L',leftBound)
# print('R',rightBound)

leftArr = []
leftS = sum(leftBound.values())
for i in range(low, high + 1):
    leftArr.append(totalL)
    if i in leftBound:
        leftS -= leftBound[i]
    totalL -= leftS

rightArr = []
rightS = sum(rightBound.values())
for i in range(high, low - 1, -1):
    rightArr.append(totalR)
    if i in rightBound:
        rightS -= rightBound[i]
    # print(rightS)
    totalR -= rightS

# print('L',leftArr)
# print('R',rightArr)

minS = float('inf')
for i in range(len(rightArr)):
    s = rightArr[i] + leftArr[len(rightArr) - i - 1]
    # print(s)
    if s < minS:
        minS = s

print(minS)