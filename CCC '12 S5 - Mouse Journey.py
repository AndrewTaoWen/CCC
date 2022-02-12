Rows, Cols = input().split()
Rows = int(Rows)
Cols = int(Cols)

m = []
cats = []
K = int(input())

for i in range(Rows + 1):
    row = []
    cat = []
    for i in range(Cols + 1):
        row.append(0)
        cat.append(True)
    m.append(row)
    cats.append(cat)

for i in range(K):
    a, b = input().split()
    a = int(a)
    b = int(b)
    m[a][b] = 0
    cats[a][b] = False

m[1][1] = 1
cats[1][1] = False

for i in range(1, Rows + 1):
    for j in range(1, Cols + 1):
        # print(a)
        if cats[i][j] == True:
            m[i][j] = m[i - 1][j] + m[i][j - 1]

print(m[-1][-1])