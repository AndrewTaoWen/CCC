l = list(input())

clubs = []
diamonds = []
hearts = []
spades = []

c = False
d = False
h = False
s = False

for i in l:
    if c == True:
        clubs.append(i)
    if d == True:
        diamonds.append(i)
    if h == True:
        hearts.append(i)
    if s == True:
        spades.append(i)
    if i == 'C':
        c = True
    elif i == 'D':
        d = True
        c = False
    elif i == 'H':
        d = False
        h = True
    elif i == 'S':
        h = False
        s = True

clubs.pop()
diamonds.pop()
hearts.pop()

cPoints = 0
dPoints = 0
hPoints = 0
sPoints = 0

suits = [clubs,diamonds,hearts,spades]

for i in range(4):
    pts = 0
    if len(suits[i]) == 0:
        pts += 3
    elif len(suits[i]) == 1:
        pts += 2
    elif len(suits[i]) == 2:
        pts += 1

    # print(suits[i])

    for j in suits[i]:
            if j == 'A':
                pts += 4
            elif j == 'K':
                pts += 3
            elif j == 'Q':
                pts += 2
            elif j == 'J':
                pts += 1

    if i == 0:
        cPoints = pts
    elif i == 1:
        dPoints = pts
    elif i == 2:
        hPoints = pts
    elif i == 3:
        sPoints = pts

    suits[i] = ' '.join(suits[i])


print('Cards Dealt              Points')
if suits[0] == '':
    print(f"Clubs {23*' '} {cPoints}")
else:
    print(f"Clubs {suits[0]}{(24-(len(clubs)*2))*' '} {cPoints}")

if suits[1] == '':
    print(f"Diamonds {20*' '} {dPoints}")
else:
    print(f"Diamonds {suits[1]}{(21-(len(diamonds)*2))*' '} {dPoints}")

if suits[2] == '':
    print(f"Hearts {22*' '} {hPoints}")
else:
    print(f"Hearts {suits[2]}{(23-(len(hearts)*2))*' '} {hPoints}")

if suits[3] == '':
    print(f"Spades {22*' '} {sPoints}")
else:
    print(f"Spades {suits[3]}{(23-(len(spades)*2))*' '} {sPoints}")

print(f'                       Total {cPoints+dPoints+hPoints+sPoints}')
