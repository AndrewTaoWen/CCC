a = int(input())


def isprime(num):
    isprime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isprime = False
            break

    return isprime


for _ in range(a):
    b = int(input())
    for i in range(2, 2 * b + 1):
        if isprime(i) == True:
            if isprime(2 * b - i) == True:
                print(i, (2 * b) - i)
                break
