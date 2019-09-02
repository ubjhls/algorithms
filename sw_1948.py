testcase = int(input())

for i in range(testcase):
    date = list(map(int, input().split()))
    count_1 = 0
    count_2 = 0

    for j in range(1, date[0]):
        if j < 8:
            if j == 2:
                count_1 += 28
            elif j % 2 == 0:
                count_1 += 30
            elif j % 2 == 1:
                count_1 += 31
        elif j >= 8:
            if j % 2 == 0:
                count_1 += 31
            elif j % 2 == 1:
                count_1 += 30
    count_1 += date[1]

    for j in range(1, date[2]):
        if j < 8:
            if j == 2:
                count_2 += 28
            elif j % 2 == 0:
                count_2 += 30
            elif j % 2 == 1:
                count_2 += 31
        elif j >= 8:
            if j % 2 == 0:
                count_2 += 31
            elif j % 2 == 1:
                count_2 += 30
    count_2 += date[3]
    tmp = count_2 - count_1 + 1
    print('#{} {}'.format(i+1,tmp))