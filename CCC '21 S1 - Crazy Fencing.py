numFence = int(input())

heightLF = input().split(' ')

heightBottom = input().split(' ')

areaFence = 0

for i in range(numFence):

    areaFence += (abs(int(heightLF[i + 1]) - int(heightLF[i])) * int(heightBottom[i])) / 2

    if int(heightLF[i + 1]) > int(heightLF[i]):
        areaFence += int(heightLF[i]) * int(heightBottom[i])

    else:
        areaFence += int(heightLF[i + 1]) * int(heightBottom[i])

print(areaFence)