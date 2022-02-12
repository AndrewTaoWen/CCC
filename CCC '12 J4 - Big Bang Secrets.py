a = int(input())
b = input()

alphabet = []
for letter in range(65, 91):
    alphabet.append(chr(letter))

c = []

for i in b:
  c.append([int(x) for x in range(len(alphabet)) if alphabet[x] == i])

for i in range(len(b)):
  c[i][0] -= ((3*(i+1)+a))

output = ''

for i in range(len(c)):
  output += str(alphabet[c[i][0]])

print(output)