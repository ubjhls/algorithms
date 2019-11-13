T = int(input())

for i in range(T):
    card = input()
    tmp = [[] for _ in range(len(card) // 3)]
    result = [13] * 4
    real_result = ''
    count = 0
    for j in range(0, len(card), 3):
        for k in range(j, j+3):
            tmp[count].append(card[k])
        count += 1

    for j in range(len(card) // 3):
        if tmp[j][0] == "S":
            result[0] = result[0] - 1
        elif tmp[j][0] == "D":
            result[1] = result[1] - 1
        elif tmp[j][0] == "H":
            result[2] = result[2] - 1
        elif tmp[j][0] == "C":
            result[3] = result[3] - 1

    for j in range(len(card) // 3):
        for k in range(len(card) // 3):
            if j != k:
                if tmp[j] == tmp[k]:
                    result = ['ERROR']
                    break
    if len(result) == 1:
        real_result += 'ERROR'
    else:
        real_result += ' '.join(map(str, result))

    print('#{} {}'.format(i + 1, real_result))

