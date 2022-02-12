n = int(input())
M = []

for _ in range(n):
  M.append(list(map(int, input().split(' '))))

for k in range(4):
  if M[0][0] < M[0][1] and M[0][0] < M[1][0]:
    for i in M:
        print(*i)
    break
  rotatedM = [[0 for x in range(n)] for x in range(n)]
  for i in range(n):
    for j in range(n):
      rotatedM[j][n-1-i] = M[i][j]
  M = rotatedM
