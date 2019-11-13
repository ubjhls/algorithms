from itertools import permutations
T = int(input())
for t in range(1, T + 1):
    num = list(map(int, input().split()))
    number = input()
    tmp = []
    count_tmp = 0
    result = []
    count = 0
    ans = []
    for i in range(10):
        if num[i] != 0:
            tmp.append(i)
    for i in range(len(number)):
        if int(number[i]) not in tmp:
            break
        count_tmp += 1

    if len(number) == count_tmp:
        print('#{} {}'.format(t, count_tmp + 1))
    else:
        for m in range(len(number) + 1):
            for i in permutations(tmp, m):

                ex = ''
                for j in i:
                    ex += str(j)
                result.append(ex)
        for m in range(1, len(result)):
            for i in range(1, len(result)):

                count = 0
                if int(result[m]) * int(result[i]) == int(number):
                    count = len(result[m]) + len(result[i]) + 2
                    ans.append(count)
        if len(ans) == 0:
            print('#{} {}'.format(t, -1))
        else:
            print('#{} {}'.format(t, min(ans)))