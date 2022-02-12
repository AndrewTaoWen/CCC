n, rounds = input().split()

n = int(n)
rounds = int(rounds)

l = [0 for i in range(n)]

ranks = [[] for i in range(n)]


def findRank(arr, target):
    arr = sorted(arr, reverse=True)
    # print(arr)
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1


for i in range(rounds):
    curL = [int(k) for k in input().split(' ')]
    for i in range(n):
        l[i] += curL[i]

    for i in range(n):
        ranks[i].append(findRank(l, l[i]))

m = max(l)
for i in range(n):
    if l[i] == max(l):
        # print(i)
        print(f'Yodeller {i + 1} is the TopYodeller: score {m}, worst rank {max(ranks[i])}')
