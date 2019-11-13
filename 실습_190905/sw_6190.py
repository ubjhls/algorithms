T = int(input())

for i in range(T):
    num = int(input())
    increase = list(map(int, input().split()))
    result = []

    for j in range(num):
        for m in range(j+1, num):
            count = 0
            tmp = increase[j] * increase[m]
            tmp = str(tmp)
            if len(tmp) == 1:
                result.append(int(tmp))
            else:
                for k in range(len(tmp) - 1):
                    if tmp[k] <= tmp[k+1]:
                        count += 1
                    if len(tmp)-1 == count:
                        result.append(int(tmp))
                        break
            if not(result):
                result.append(-1)

    print('#{} {}'.format(i+1, max(result)))