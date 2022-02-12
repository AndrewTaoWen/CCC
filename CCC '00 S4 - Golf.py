d = int(input())
numC = int(input())
clubs = []

for _ in range(numC):
    clubs.append(int(input()))

visited = set()
count = 1
position = clubs

notReached = True
defeat = False

while notReached:
    for i in position:
        if i < d:
            break
    else:
        notReached = False
        defeat = True

    count += 1
    currentP = []
    for i in position:
        for j in clubs:
            k = i + j
            if k not in visited:
                visited.add(k)
                currentP.append(k)
    position = currentP
    # print(position)

    for i in position:
        if i == d:
            notReached = False
            break

if defeat == True:
    print('Roberta acknowledges defeat.')
else:
    print('Roberta wins in', count, 'strokes.')
