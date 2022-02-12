num = int(input())

vowel = {'a', 'e', 'i', 'o', 'u'}


def findSyllable(l):
    syl = ''
    # print(len(l))
    n = 0
    for i in range(len(l) - 1, 0, -1):
        syl += l[i]
        if l[i] in vowel:
            n = i
            break

    syl += l[n]

    return syl


for _ in range(num):
    l1 = input().split(' ')
    l2 = input().split(' ')
    l3 = input().split(' ')
    l4 = input().split(' ')

    l1 = l1[-1].lower()
    l2 = l2[-1].lower()
    l3 = l3[-1].lower()
    l4 = l4[-1].lower()

    syl1 = findSyllable(l1)
    syl2 = findSyllable(l2)
    syl3 = findSyllable(l3)
    syl4 = findSyllable(l4)

    # print(syl1, syl2, syl3, syl4)

    if syl1 == syl2 and syl3 == syl4 and syl2 != syl3:
        print('even')

    elif syl1 == syl2 == syl3 == syl4:
        print('perfect')

    elif syl1 == syl4 and syl2 == syl3:
        print('shell')

    elif syl1 == syl3 and syl2 == syl4:
        print('cross')

    else:
        print('free')