a = int(input())
b = int(input())
c = int(input())
d = int(input())

pick = 'answer'

if a == 8 or a == 9:
    if b == c:
        if d == 8 or d == 9:
            pick = 'ignore'

print(pick)