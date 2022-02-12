num = int(input())
highest = 0
highestP = ''
for _ in range(num):
    person = input()
    amount = int(input())
    if amount > highest:
        highest = amount
        highestP = person

print(highestP)