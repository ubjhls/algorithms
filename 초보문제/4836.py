testcase = int(input())

for m in range(testcase):
    tmp = []
    arr = [[0] * 10 for i in range(10)]
    bound = int(input())
    count = 0
    for i in range(bound):
        tmp.append(list(map(int,input().split())))

    for i in range(bound):
        for j in range(tmp[i][0],tmp[i][2]+1):
            for k in range(tmp[i][1],tmp[i][3]+1):
                arr[j][k] += tmp[i][4]

    for r in range(10):
        for t in range(10):
            if arr[r][t] == 3:
                count+=1
    print('#{} {}'.format(m+1,count))
