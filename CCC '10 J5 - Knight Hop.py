start = input().split()
end = input().split()

start = (int(start[0]), int(start[1]))
end = (int(end[0]), int(end[1]))

Q = []

Q.append(start)

counter = -1
MOVES = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2, 1), (-1,2)]

while Q:
    counter += 1
    size = len(Q)
    for i in range(size):
      cp = Q.pop(0)
      # print(cp)
      if cp == end:
        break
      for m in MOVES:
        x = cp[0]+m[0]
        y = cp[1]+m[1]
        if x <= 8 and x >= 1 and y <= 8 and y >= 1:
          Q.append((x,y))

    else:
      continue
    break

print(counter)