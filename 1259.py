testcase = int(input())

for i in range(testcase):
    number = int(input())
    real_bar = [[0]*2 for _ in range(number)]
    bar = list(map(int, input().split()))
    count = 0
    count_2 = 0
    print('#{}'.format(i + 1), end=' ')
    for j in range(number):
        for k in range(2):
            real_bar[j][k] = bar[count]
            count += 1
    for k in range(number-1):
        for j in range(2):
            tmp = []
            if real_bar[k][0] == real_bar[k+j][1]:
                tmp.append(real_bar[k+j])
                del real_bar[k+j]
                real_bar.insert(0,tmp)

    for j in range(number):
        for k in range(2):
            result = ''
            result += str(real_bar[j][k])
            count_2 += 1
            print(result,end = ' ')
            if count_2 == 2*number:
                print('')