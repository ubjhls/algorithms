testcase = int(input())
for k in range(testcase):
    test = list(map(int, input().split()))
    score = [list(map(int, input().split())) for i in range(test[0])]

    result = []

    for i in range(test[0]):
        tmp = 0
        tmp = score[i][0]*35 + score[i][1]*45 + score[i][2]*20
        result.append(tmp)
    result_tmp = result[test[1]-1]
    result.sort()
    result = result[::-1]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(test[0]):
        if result[i] == result_tmp:
            print('#{} {}'.format(k+1, grade[i//(test[0]//10)]))