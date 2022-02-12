a,b = input().split()
xMax = int(a)
yMax = int(b)

position = [0,0]
while True:
    a,b = input().split()
    if a == '0' and b == '0':
        break
    xMove = int(a)
    yMove = int(b)
    newPositionX = position[0] + xMove
    newPositionY = position[1] + yMove
    if newPositionX > xMax:
        newPositionX = xMax
    elif newPositionX < 0:
        newPositionX = 0
    if newPositionY > yMax:
        newPositionY = yMax
    elif newPositionY < 0:
        newPositionY = 0
    position[0] = newPositionX
    position[1] = newPositionY
    print(f'{position[0]} {position[1]}')
