num = int(input())
m = int(input())
n = int(input())

grid = []
for i in range(m):
    grid.append(list(input()))

s = 0
rooms = []

for i in range(m):
    for j in range(n):

        if grid[i][j] == "I":
            continue

        else:
            stack = list()
            stack.append([i, j])
            curRoom = set()

            while len(stack) != 0:

                [r, c] = stack.pop()
                curRoom.add((r, c))

                if r >= 1 and grid[r - 1][c] == ".":
                    stack.append([r - 1, c])

                if r < m - 1 and grid[r + 1][c] == ".":
                    stack.append([r + 1, c])

                if c >= 1 and grid[r][c - 1] == ".":
                    stack.append([r, c - 1])

                if c < n - 1 and grid[r][c + 1] == ".":
                    stack.append([r, c + 1])

                    # mark as visited
                grid[r][c] = 'I'

            curLen = len(curRoom)

            rooms.append(curLen)

            s += 1

fRoom = sorted(rooms)

# print(fRoom)

cnt = 0

while fRoom:

    curN = fRoom.pop()
    # print(num)
    num -= curN
    if num < 0:
        num += curN
        break

    cnt += 1

if cnt == 1:
    print(f'{1} room, {num} square metre(s) left over')
else:
    print(f'{cnt} rooms, {num} square metre(s) left over')
