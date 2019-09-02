testcase = int(input())

for i in range(testcase):
    test = list(map(int, input().split()))
    number_1 = list(map(int, input().split()))
    number_2 = list(map(int, input().split()))
    result = []
    if len(number_1) < len(number_2):
        for k in range(len(number_2)-len(number_1)+1):
            tmp = 0
            for j in range(len(number_1)):
                tmp += number_1[j] * number_2[j+k]
            result.append(tmp)
        print('#{} {}'.format(i+1, max(result)))
    else:
        for k in range(len(number_1)-len(number_2)+1):
            tmp = 0
            for j in range(len(number_2)):
                tmp += number_2[j] * number_1[j+k]
            result.append(tmp)
        print('#{} {}'.format(i+1, max(result)))