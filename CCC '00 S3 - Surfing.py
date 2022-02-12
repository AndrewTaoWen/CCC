num = int(input())

g = {}
# d = {}
# b = 0

for i in range(num):
    page = input()
    while True:
        line = input()
        if line == '</HTML>':
            break
        for i in range(len(line)):
            if line[i:i+5] == 'HREF=':
                # print(True)
                link = ''
                k = i+6
                while line[k] != '"':
                    link += line[k]
                    k += 1
                # if link not in d:
                #     d[link] = b
                #     b += 1
                g[page] = g.get(page,()) + (link,)
                # g[link] = g.get(link,(page,)) + (page,)
    if page not in g:
        g[page] = ()

r = []
while True:
    l1 = input()
    if l1 == 'The End':
        break
    l2 = input()
    v = set()
    q = [l1]
    found = False
    # path = []
    while q:
        curV = q.pop(0)
        for i in g[curV]:
            if i == l2:
                found = True
                break
            if i not in v:
                q.append(i)
                v.add(i)
                # print(f'Link from {curV} to {i}')

        if found:
            # for i in path:
                # a,b = i
                # print(f'Link from {a} to {b}')
            r.append(f'Can surf from {l1} to {l2}.')
            break
    else:
        r.append(f"Can't surf from {l1} to {l2}.")

for i in g.keys():
    for j in g[i]:
        print(f'Link from {i} to {j}')

for i in r:
    print(i)