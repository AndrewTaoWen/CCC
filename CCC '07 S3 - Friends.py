N = int(input())
edges = {}

for _ in range(N):
    start, end = map(int, input().split())
    edges[start] = end

while True:
    s, e = map(int, input().split())

    if s == 0 and e == 0:
        break

    queue = [s]
    cnt = 0
    visited = set()

    Found = False
    while queue:
        curNode = queue.pop(0)
        nextNode = edges[curNode]
        if nextNode == e:
            print('Yes', cnt)
            break
        if nextNode not in visited:
            visited.add(nextNode)
            queue.append(nextNode)

        cnt += 1
    else:
        print('No')
