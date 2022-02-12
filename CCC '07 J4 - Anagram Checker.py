a = input()
b = input()

mA = {}
mB = {}

for i in a:
  if i == ' ':
    continue
  if i not in mA:
    mA[i] = 1
  else:
    mA[i] += 1

for i in b:
  if i == ' ':
    continue
  if i not in mB:
    mB[i] = 1
  else:
    mB[i] += 1

if mA == mB:
  print('Is an anagram.')
else:
  print('Is not an anagram.')
