instructions = []

while True:
    ins = input()
    instructions.append(ins)
    if ins == 'SCHOOL':
        break

for i in range(len(instructions)-1,0,-1):
    # print(i)
    if instructions[i] == 'R':
        print('Turn LEFT onto', instructions[i-1], 'street.')
    elif instructions[i] == 'L':
        print('Turn RIGHT onto', instructions[i-1], 'street.')
    elif i == 1:
        if instructions[0] == 'R':
            print('Turn LEFT into your HOME.')
        else:
            print('Turn RIGHT into your HOME.')
