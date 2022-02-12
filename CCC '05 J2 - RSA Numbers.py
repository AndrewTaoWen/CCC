num1 = int(input())
num2 = int(input()) + 1

numRSA = 0

for i in range(num1, num2):
    count = 0
    d = []
    for k in range(1, int(i ** 0.5) + 1):
        if i % k == 0:
            if i // k != k:
                # d.append(i // k)
                # d.append(k)
                count += 2
            else:
                # d.append(k)
                count += 1
    # print(d)
    if count == 4:
        numRSA += 1

print('The number of RSA numbers between', num1, 'and', num2 - 1, 'is', numRSA)
