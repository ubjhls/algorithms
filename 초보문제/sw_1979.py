import copy

T = int(input())

for index in range(1, T + 1):

    n, k = map(int, input().split())
    p = [[x for x in input().split()] for _ in range(n)]
    result = 0

    for i in range(n):
        result += ''.join(p[i]).split('0').count('1' * k)

    temp = copy.deepcopy(p)
    for i in range(n):
        for j in range(n):
            temp[i][j] = p[j][i]
    for i in range(n):
        result += ''.join(temp[i]).split('0').count('1' * k)
    print('#{} {}'.format(index, result))