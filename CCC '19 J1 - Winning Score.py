applethree = int(input()) * 3
appletwo = int(input()) * 2
apple = int(input())
scoreA = applethree + appletwo + apple

threebanana = int(input()) * 3
twobanana = int(input()) * 2
banana = int(input())
scoreB = threebanana + twobanana + banana

if scoreA > scoreB:
    print('A')
elif scoreA == scoreB:
    print('T')
else:
    print('B')