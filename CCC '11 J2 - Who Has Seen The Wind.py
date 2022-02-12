hum = int(input())
t = int(input())

# print(hum)
# print(t)

s = set()

for i in range(1, t+1):
    A = -6*(i**4) + hum*(i**3) + 2*(i**2) + i
    if A <= 0:
        print(f'The balloon first touches ground at hour:')
        print(i)
        break
    # s.add(i)
else:
    print('The balloon does not touch ground in the given time.')
