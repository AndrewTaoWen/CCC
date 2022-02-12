n, m = map(int, input().split())

CON = {'U', 'D', 'L', 'R'}

grid = []
for _ in range(n):
    grid.append(list(input()))

x = 0
y = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            x, y = i, j

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'C':
            num = i + 1
            while grid[num][j] != "W" and grid[num][j] != 'C':
                if grid[num][j] in CON:
                    pass
                else:
                    grid[num][j] = 'X'
                num += 1
            num = i - 1
            while grid[num][j] != 'W' and grid[num][j] != 'C':
                if grid[num][j] in CON:
                    pass
                else:
                    grid[num][j] = 'X'
                num -= 1
            num = j + 1
            while grid[i][num] != "W" and grid[i][num] != 'C':
                if grid[i][num] in CON:
                    pass
                else:
                    grid[i][num] = 'X'
                num += 1
            num = j - 1
            while grid[i][num] != "W" and grid[i][num] != 'C':
                if grid[i][num] in CON:
                    pass
                else:
                    grid[i][num] = 'X'
                num -= 1

DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))

if grid[x][y] == 'S':
    queue = [[x, y, 0]]

    while queue:
        # print(queue)
        [r, c, num] = queue.pop(0)

        for dx, dy in DIR:
            mx = dx + r
            my = dy + c
            # print(mx,my)

            while grid[mx][my] in CON:
                if grid[mx][my] == 'U':
                    # print('u',mx,my)
                    grid[mx][my] = 'V'
                    mx -= 1

                elif grid[mx][my] == 'D':
                    grid[mx][my] = 'V'
                    mx += 1

                elif grid[mx][my] == 'L':
                    grid[mx][my] = 'V'
                    my -= 1

                elif grid[mx][my] == 'R':
                    grid[mx][my] = 'V'
                    my += 1

            if grid[mx][my] == '.':
                grid[mx][my] = (num + 1)
                queue.append([mx, my, num + 1])

for i in range(n):
    for j in range(m):
        if i == x and j == y:
            continue
        if grid[i][j] == 'X' or grid[i][j] == '.':
            print(-1)
        elif isinstance(grid[i][j], int):
            print(grid[i][j])