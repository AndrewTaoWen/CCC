g1 = list(input())
g2 = list(input())
numTest = int(input())

upper = {'A','B','C','D','E'}

possible = set()

for i in range(0, 10, 2):
    curP = (g1[i],g1[i+1],g2[i],g2[i+1])
    # print(curP)
    if curP[0] in upper and curP[1] in upper:
        possible.add(curP[0])
    elif curP[2] in upper and curP[3] in upper:
        possible.add(curP[2])
    elif curP[0] not in upper and curP[1] not in upper and curP[2] not in upper and curP[3] not in upper:
        possible.add(curP[0])
    else:
        possible.add(curP[0].upper())
        possible.add(curP[0].lower())



for i in range(numTest):
    possibleGene = input()
    for i in possibleGene:
        if i not in possible:
            print('Not their baby!')
            break
    else:
        print('Possible baby.')