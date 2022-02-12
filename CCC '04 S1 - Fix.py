numTest = int(input())

for _ in range(numTest):
    fixfree = True
    a = input()
    b = input()
    c = input()
    fixes = set()
    for i in range(1, len(a) + 1):
        fixes.add(a[:i])
        fixes.add(a[i:])
    if b in fixes or c in fixes:
        fixfree = False
    fixes = set()
    for i in range(1, len(b) + 1):
        fixes.add(b[:i])
        fixes.add(b[i:])
    if a in fixes or c in fixes:
        fixfree = False
    fixes = set()
    for i in range(1, len(c) + 1):
        fixes.add(c[:i])
        fixes.add(c[i:])
    if a in fixes or b in fixes:
        fixfree = False

    if fixfree == True:
        print('Yes')
    else:
        print('No')
