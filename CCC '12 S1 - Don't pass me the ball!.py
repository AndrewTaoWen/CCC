a = int(input())
# b = []

def factorial(num):
  f = 1
  for i in range(1,num+1):
    f = f * i
  return int(f)

if a > 4:
  possibilities = factorial(a-1)/(6*factorial(a-4))
  print(int(possibilities))
elif a == 4:
  print(1)
else:
  print(0)
