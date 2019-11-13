test = list(map(int, input().split()))
result = []
for i in range(test[0]):
    arr = list(map(str, input()))
    tmp = []
    for j in arr:
        tmp.append(j)
    result.append(tmp)
count_tmp = []
for i in range(test[0]):
    for k in range(test[1]-8):
        count = 0
        for j in range(i+k, i+k+8):
            if result[i][j] == result[i][j+1]:
                if result[i][j] == 'W':
                    result[i][j+1] = 'B'
                    count += 1
                else:
                    result[i][j+1] = 'W'
                    count += 1
            else:
                continue
print(count)