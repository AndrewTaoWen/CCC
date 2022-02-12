word = input()
palindromes = []

a = len(word)

for i in range(0,a+1):
    for j in range(i,a+1):
            w = word[i:j]
            if w == w[::-1]:
                palindromes.append(len(w))

print(max(palindromes))