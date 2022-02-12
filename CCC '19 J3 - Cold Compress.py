numCase = int(input())

for _ in range(numCase):
    case = list(input())
    string = ''
    currentChar = case[0]
    currentCount = 0
    for i in case:
        if i != currentChar:
            string += f'{currentCount} {currentChar} '
            currentChar = i
            currentCount = 1
        else:
            currentCount += 1
    string += f'{currentCount} {currentChar} '

    print(string)