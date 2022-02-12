while True:
    string = list(input())
    if '!' in string:
        break
    if len(string) > 4:
        if string[-3] not in 'aeiouy':
            if string[-2] == 'o' and string[-1] == 'r':
                string[-1] = 'u'
                string.append('r')
    print(''.join(string))
