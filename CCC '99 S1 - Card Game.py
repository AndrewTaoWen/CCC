highcards = {'ace', 'jack', 'queen', 'king'}
pts1 = 0
pts2 = 0

cards = []

for i in range(0, 52):
    # print(i)
    cards.append(input())
    # print(cards)

    pts = 0
    index = 0

    if i >= 1 and (i - 1) <= 51 and cards[i - 1] == 'jack':
        if cards[i] not in highcards:
            pts += 1
            index = i - 1

    elif i >= 2 and (i - 2) <= 50 and cards[i - 2] == 'queen':
        if cards[i - 1] not in highcards and cards[i] not in highcards:
            pts += 2
            index = i - 2

    elif i >= 3 and (i - 3) <= 49 and cards[i - 3] == 'king':
        if cards[i] not in highcards and cards[i - 1] not in highcards and cards[i - 2] not in highcards:
            pts += 3
            index = i - 3

    elif i >= 4 and (i - 4) <= 48 and cards[i - 4] == 'ace':
        if cards[i] not in highcards and cards[i - 1] not in highcards and cards[i - 2] not in highcards and cards[
            i - 3] not in highcards:
            pts += 4
            index = i - 4

    if pts != 0:
        if (index) % 2 == 0:
            pts1 += pts
            # print(i)
            print(f'Player A scores {pts} point(s).')
        else:
            pts2 += pts
            # print(i)
            print(f'Player B scores {pts} point(s).')

print(f'Player A: {pts1} point(s).')
print(f'Player B: {pts2} point(s).')