a, b = input().split()

print('Sun Mon Tue Wed Thr Fri Sat')

c = []

for i in range(int(b)+1):
  c.append(str(i))

if int(a) == 1 or int(a) == 0:
  print(("  " + '   '.join(c[1:8])).rstrip())
  print(("  "+ '   '.join(c[8:10])+"  "+'  '.join(c[10:15])).rstrip())
  print((" "+ '  '.join(c[15:22])).rstrip())
  if int(b) <= 28:
    print((" "+ '  '.join(c[22:29])).rstrip())
  else:
    print((" "+ '  '.join(c[22:29])).rstrip())
    print((" "+ '  '.join(c[29:int(b)+1])).rstrip())
elif 2 <= int(a) <= 6:
  print(('    ' * (int(a)-1) + "  " + '   '.join(c[1:9-int(a)])).rstrip())
  print(("  "+ '   '.join(c[9-int(a):10])+"  "+'  '.join(c[10:16-int(a)])).rstrip())
  print((" "+ '  '.join(c[16-int(a):23-int(a)])).rstrip())
  print((" "+ '  '.join(c[23-int(a):30-int(a)])).rstrip())
  if int(a) == 6 and int(b) == 31:
    print((" "+ '  '.join(c[30-int(a):31])).rstrip())
    print((" "+ '  '.join(c[31:32])).rstrip())
  else:
    print((" "+ '  '.join(c[30-int(a):int(b)+1])).rstrip())
if int(a) == 7:
  print(('    ' * (int(a)-1) + "  " + '   '.join(c[1:2])).rstrip())
  print(("  "+ '   '.join(c[2:9])).rstrip())
  print(("  "+ '  '.join(c[9:16])).rstrip())
  print((" "+ '  '.join(c[16:23])).rstrip())
  print((" "+ '  '.join(c[23:30])).rstrip())
  if int(b) == 30:
    print((" "+ str(30)).rstrip())
  elif int(b) == 31:
    print((" "+ str(30)+"  " +str(31)).rstrip())