num = int(input())

d = {}

for i in range(num):
    char, value = input().split()
    d[value] = char

binary = input()

curStr = ''

output = ''

for i in binary:
    curStr += i
    if curStr in d:
        output += d[curStr]
        curStr = ''

print(output)