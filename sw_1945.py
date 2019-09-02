testcase = int(input())

for i in range(testcase):
    number = int(input())
    tmp = 0
    num = [2, 3, 5, 7, 11]
    print('#{}'.format(i+1), end=' ')
    for k in num:
        count = 0
        while True:
            tmp = number // k
            if number % k == 0:
                number = tmp
                count += 1
                if number == k:
                    count += 1
                    print(count, end = ' ')
                    break
            else:
                print(count, end = ' ')
                break
    print('')