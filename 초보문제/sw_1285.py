T = int(input())

for i in range(T):
    testcase = int(input())
    num = list(map(int, input().split()))
    result = []
    for j in num:
        if j < 0:
            j = j * -1
            result.append(j)
        else:
            result.append(j)
    print('#{} {} {}'.format(i+1,min(result),result.count(min(result))))