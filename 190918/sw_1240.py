T = int(input())
for q in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result =[]
    tmp_1 = 0
    tmp_2 = 0
    num = {'0001101': 0, '0011001': 1,'0010011': 2,'0111101': 3,'0100011': 4,'0110001': 5,'0101111': 6,'0111011': 7,'0110111': 8,'0001011': 9}
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                for k in range(j-55, j+1, 7):
                    tmp = ''
                    for m in range(7):
                        tmp += arr[i][k+m]
                    for key, value in num.items():
                        if key == tmp:
                            result.append(value)
            if result:
                break
        if result:
            break
    for i in range(8):
        if i % 2 == 0:
            tmp_1 += result[i]
        else:
            tmp_2 += result[i]
    ans = tmp_1 * 3 + tmp_2
    if ans % 10 == 0:
        print('#{} {}'.format(q+1, sum(result)))
    else:
        print('#{} {}'.format(q+1, 0))