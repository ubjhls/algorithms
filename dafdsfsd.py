arr = [[0] * 10 for i in range(10)]

testcase = int(input())
bound = int(input())
tmp = []
for i in range(bound):
    tmp.append(list(map(int,input().split())))
    count = 0

    for k in range(bound):
        for i in range(tmp[k][0],tmp[k][2],1):
            for j in range(tmp[k][1],tmp[k][3],1):
                arr[i][j] += tmp[k][4]

    for i in range(10):
        for j in range(10):
            if arr[i][j] >= 3:
                count+=1
    print(count)
