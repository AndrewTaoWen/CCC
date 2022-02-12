friendships = [[], [6], [6], [4, 5, 6, 15], [3, 5, 6], [3, 4, 6], [1, 2, 3, 4, 5, 7], [6, 8], [7, 9], [8, 10, 12],
               [9, 11], [10, 12], [9, 11, 13], [12, 14, 15], [13], [3, 13], [17, 18], [16, 18], [16, 17], [], [], [],
               [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
               [], [], []]

while True:
    char = input()
    if char == 'q':
        break
    elif char == 'i':
        x = int(input())
        y = int(input())
        friendships[x].append(y)
        friendships[y].append(x)
        # print(friendships)
    elif char == 'd':
        x = int(input())
        y = int(input())
        friendships[x].remove(y)
        friendships[y].remove(x)
    elif char == 'n':
        x = int(input())
        print(len(friendships[x]))
    elif char == 'f':
        x = int(input())
        queue = []
        visited = {x}
        for i in friendships[x]:
            queue.append(i)
            visited.add(i)

        cnt = 0
        while queue:
            friend = queue.pop(0)
            for i in friendships[friend]:
                if i not in visited:
                    cnt += 1
                    visited.add(i)
        print(cnt)
    elif char == 's':
        start = int(input())
        end = int(input())
        queue = [(start, 0)]
        visited = {start}
        cnt = 0
        reached = False

        while queue:
            # print(queue)
            (curNode, steps) = queue.pop(0)
            for i in friendships[curNode]:
                if i == end:
                    print(steps + 1)
                    reached = True
                    break
                if i not in visited:
                    visited.add(i)
                    queue.append((i, steps + 1))

            if reached:
                break

        else:
            print('Not connected')
    # print(friendships)