testcase = int(input())
for p in range(testcase):

    test = list(map(int, input().split()))
    string = [input() for i in range(test[0])]
    print('#{} '.format(p+1), end ='')
    for i in range(test[0]):
        for j in range(test[0]-test[1]+1):
            count = 0
            if string[i][j] == string[i][j+test[1]-1]:
                for k in range(test[1] // 2):
                    if string[i][j+k] == string[i][j+test[1]-1-k]:
                        count += 1
                    else:
                        break
            if count == test[1] // 2:
                for w in range(test[1]):
                    print('{}'.format(string[i][j+w]),end='')
                break
        if count == test[1] // 2:
            print('')

    for i in range(test[0]):
        for j in range(test[0]-test[1]+1):
            count = 0
            if string[j][i] == string[j+test[1]-1][i]:
                for k in range(test[1] // 2):
                    if string[j+k][i] == string[j+test[1]-1-k][i]:
                        count += 1
                    else:
                        break
            if count == test[1] // 2:
                for w in range(test[1]):
                    print('{}'.format(string[j+w][i]), end='')
                break
        if count == test[1] // 2:
            print('')