testcase = int(input())

for i in range(testcase):
    test = input()
    count = 0
    for j in range(len(test) // 2):
        if test[j] == '*' or test[-1-j] == '*':
            print('#{} {}'.format(i + 1, 'Exist'))
            break
        elif test[j] == test[-1 - j]:
            count += 1
    if len(test) // 2 == count:
        print('#{} {}'.format(i + 1, 'Exist'))
    else:
        print('#{} {}'.format(i + 1, 'Not exist'))