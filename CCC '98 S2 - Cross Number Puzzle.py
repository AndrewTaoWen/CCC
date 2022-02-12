def perfect(num):
    factors = []
    # print(factors)
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if i != 1:
                factors.append(num // i)

    # print(factors)

    if sum(factors) == num:
        return True
    else:
        return False


def cube(num):
    l = [int(i) ** 3 for i in list(str(num))]

    if num == sum(l):
        return True
    else:
        return False


numsP = []
numsC = []

for i in range(100, 1000):
    if cube(i) == True:
        numsC.append(str(i))

for i in range(1000, 10000):
    if perfect(i) == True:
        numsP.append(str(i))

print(' '.join(numsP))
print(' '.join(numsC))