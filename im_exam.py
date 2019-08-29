TC = int(input())

for i in range(TC):
    count = 0
    test = int(input())
    mol = [list(map(int, input().split())) for _ in range(test)]
    for j in range(test):
        for k in range(test):
                if mol[j][1] == mol[k][1]:
                    if mol[j][0] < mol[k][0]:
                        if mol[j][2] == 3 and mol[k][2] == 2:
                            count += mol[j][3]
                            count += mol[k][3]
                            mol[j] = [0, 0, 10, 10]
                            mol[k] = [0, 0, 10, 10]
                    elif mol[j][0] > mol[k][0]:
                        if mol[j][2] == 2 and mol[k][2] == 3:
                            count += mol[j][3]
                            count += mol[k][3]
                            mol[j] = [0, 0, 10, 10]
                            mol[k] = [0, 0, 10, 10]

                if mol[j][0] == mol[k][0]:
                    if mol[j][1] > mol[k][1]:
                        if mol[j][2] == 1 and mol[k][2] == 0:
                            count += mol[j][3]
                            count += mol[k][3]
                            mol[j] = [0, 0, 10, 10]
                            mol[k] = [0, 0, 10, 10]
                    elif mol[j][1] < mol[k][1]:
                        if mol[j][2] == 0 and mol[k][2] == 1:
                            count += mol[j][3]
                            count += mol[k][3]
                            mol[j] = [0, 0, 10, 10]
                            mol[k] = [0, 0, 10, 10]
    print(count)