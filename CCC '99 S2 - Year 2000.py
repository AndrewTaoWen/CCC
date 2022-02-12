num = int(input())

months = {'January','February','March','April','May','June','July','August','September','October','November','December'}

for _ in range(num):
    string = input().split(' ')
    # print(string)
    for i in range(len(string)):
        # print(string[i+2])
        # if string[i] in months and (0 <= i <= len(string)-2):
        # print(i)
        if string[i] in months:
            # print('i')
            if 0 <= i < (len(string)-2):
                if len(string[i+1]) == 2 or len(string[i+1]) == 3:
                    if len(string[i+2]) == 2 or len(string[i+2]) == 3:
                        s1 = string[i+1].strip(',')
                        s2 = string[i+2].strip(',')
                        if s1.isnumeric() == False or s2.isnumeric() == False:
                            continue
                        else:
                            if 1 <= int(s1) <= 31:
                                if int(s2) >= 25:
                                    string[i+2] = '19' + string[i+2]
                                else:
                                    string[i+2] = '20' + string[i+2]

        if len(string[i]) >= 8:
            # print('y')
            # print(string[i])
            if string[i][2] == string[i][5]:
                    # print('n')
                    if string[i][2] == '.':
                        d = string[i].split('.')
                        if 1 <= int(d[1]) <= 12 and 1 <= int(d[2]) <= 31:
                            if d[2][-1] == ',' or len(d[2]) == 2:
                                if int(d[0]) > 26:
                                    d[0] = '19' + d[0]
                                else:
                                    d[0] = '20' + d[0]

                    elif string[i][2] == '/':
                        # print('k')
                        d = string[i].split('/')
                        # print(d)
                        if 1 <= int(d[0]) < 31 and 1 <= int(d[1]) <= 12:
                            if d[2][-1] == ',' or len(d[2]) == 2:
                                    if int(d[2][0:2]) > 26:
                                        d[2] = '19' + d[2]
                                    else:
                                        d[2] = '20' + d[2]

                    string[i] = string[i][2].join(d)

    print(' '.join(string))