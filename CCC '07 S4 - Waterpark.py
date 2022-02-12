num = int(input())

g = [[] for i in range(num+1)]
dp = [0 for i in range(num+1)]
dp[num] = 1

while True:
    pair = input()
    # print(pair)
    if pair == '0 0':
        break
    V1, V2 = pair.split(' ')
    V1 = int(V1)
    V2 = int(V2)
    g[V2].append(V1)

for i in range(num, -1, -1):
    for j in range(len(g[i])):
        # print(i,j)
        # print(g[i][j])
        # print(dp)
        dp[g[i][j]] += dp[i]

print(dp[1])