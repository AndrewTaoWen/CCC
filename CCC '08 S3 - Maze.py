N = int(input())

for i in range(N):
    R = int(input())
    C = int(input())

    grid = []
    for i in range(R):
        grid.append(list(input()))

    queue = [(0,0,1)]
    cnt = 0
    visited = {(0,0)}

    while queue:
        # print(queue)
        # print(visited)
        curNode = queue.pop(0)
        r,c,steps = curNode[0],curNode[1],curNode[2]
        # print(y,c)
        # print(grid[0][0])
        if r == R-1 and c == C-1:
            print(steps)
            break
        if grid[r][c] == '|':
            # print('r')
            if r-1 >= 0:
                node = (r-1,c)
                if node not in visited and grid[r-1][c] != '*':
                    visited.add(node)
                    queue.append((r-1,c,steps+1))
            if r+1 <= R-1:
                node = (r+1,c)
                if node not in visited and grid[r+1][c] != '*':
                    visited.add(node)
                    queue.append((r+1,c,steps+1))
        if grid[r][c] == '-':
            if c-1 >= 0:
                node = (r,c-1)
                if node not in visited and grid[r][c-1] != '*':
                    visited.add(node)
                    queue.append((r,c-1,steps+1))
            if c+1 <= C-1:
                node = (r,c+1)
                if node not in visited and grid[r][c+1] != '*':
                    visited.add(node)
                    queue.append((r,c+1,steps+1))
        if grid[r][c] == '+':
            if r-1 >= 0:
                node = (r-1,c)
                if node not in visited and grid[r-1][c] != '*':
                    visited.add(node)
                    queue.append((r-1,c,steps+1))
            if r+1 <= R-1:
                node = (r+1,c)
                if node not in visited and grid[r+1][c] != '*':
                    visited.add(node)
                    queue.append((r+1,c,steps+1))
            if c-1 >= 0:
                node = (r,c-1)
                if node not in visited and grid[r][c-1] != '*':
                    visited.add(node)
                    queue.append((r,c-1,steps+1))
            if c+1 <= C-1:
                node = (r,c+1)
                if node not in visited and grid[r][c+1] != '*':
                    visited.add(node)
                    queue.append((r,c+1,steps+1))
    else:
        print(-1)