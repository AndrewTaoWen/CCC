x = int(input())
y = int(input())

room = []
d = []

m = 0
for i in range(x):
    room.append([])
    for j in input().split():
        k = int(j)
        if k > m:
            m = k
        room[i].append(k)

# print(room)

d = [[] for _ in range(m+1)]

for i in range(x):
    for j in range(y):
        if (i+1)*(j+1) <= m:
            d[(i+1)*(j+1)].append((i,j))

def dfs(end):
    # visited = {(0,0)}
    stack = [(0,0)]
    while stack:
        x,y = stack.pop()
        val = room[x][y]
        room[x][y] = 0
        for nx,ny in d[val]:
            if (nx,ny) == end:
                print('yes')
                return
            if room[nx][ny] != 0:
                stack.append((nx,ny))
                # room[nx][ny] = -1
                # visited.add(i)
    print('no')

dfs((x-1,y-1))
