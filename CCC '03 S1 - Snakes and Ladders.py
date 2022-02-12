b = 1

while True:
  # if input does not satisfy
  a = int(input())
  if a > 12 or a < 2:
    print('You Quit!')
    break
  # if input does satisfy
  else:
    b = (b + a)
    # snakes
    if b == 54:
      b = 19
    elif b == 90:
      b = 48
    elif b == 99:
      b = 77
    # ladders
    elif b == 40:
      b = 64
    elif b == 9:
      b = 34
    elif b == 67:
      b = 86
    # over 100
    elif b > 100:
      b = (b - a)
    # win
    print('You are now on square ' + str(b))
    if b == 100:
      print('You Win!')
      break
