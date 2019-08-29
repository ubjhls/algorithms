testcase = int(input())

for i in range(testcase):
    result = []
    tmp = []
    case = list(map(int, input().split()))
    arr = [[0] * (case[1]+1) for _ in range(case[0]+1)]
    for j in range(case[2]):
        m = list(map(int, input().split()))
        for k in range(m[0], m[2]+1):
            for p in range(m[1], m[3]+1):
                if arr[k][p] < m[4]:
                    arr[k][p] = m[4]

    for j in range(case[1]):
        for k in range(case[0]):
            result.append(arr[j][k])
    for j in range(0, 11):
        tmp.append(result.count(j))
    print('#{} {}'.format(i+1, max(tmp)))
