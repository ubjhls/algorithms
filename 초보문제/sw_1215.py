for w in range(10):
    testcase = int(input())
    string = [input() for i in range(8)]
    count = 0
    for i in range(8):
        for j in range(8-testcase+1):
            tmp = 0
            if string[i][j] == string[i][j+testcase-1]:
                for k in range(testcase // 2):
                    if string[i][j+k] == string[i][j+testcase-k-1]:
                        tmp += 1
                    else:
                        break
                if tmp == testcase // 2:
                    count += 1

    for i in range(8):
        for j in range(8-testcase+1):
            tmp = 0
            if string[j][i] == string[j+testcase-1][i]:
                for k in range(testcase // 2):
                    if string[j+k][i] == string[j+testcase-k-1][i]:
                        tmp += 1
                    else:
                        break
                if tmp == testcase // 2:
                    count += 1
    print('#{} {}'.format(w+1,count))