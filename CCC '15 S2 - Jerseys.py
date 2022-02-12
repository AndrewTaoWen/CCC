numJ = int(input())
numA = int(input())

jerseys = {}

for i in range(1,numJ+1):
    s = input()
    if s not in jerseys:
        jerseys[i] = s

# print(jerseys)

athletes = set()

for _ in range(numA):
    size,num = input().split()
    num = int(num)
    athletes.add((num,size))

# print(athletes)

count = 0

usednum = set()

for pref in athletes:
    jerseynum = pref[0]
    if jerseynum not in usednum:
        if jerseys[jerseynum] == pref[1]:
            count += 1
            usednum.add(jerseynum)
        elif jerseys[jerseynum] == 'L' or jerseys[jerseynum] == 'M':
            if pref[1] == 'M' or pref[1] == 'S':
                count += 1
                usednum.add(jerseynum)

print(count)