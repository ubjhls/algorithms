case = int(input())
for i in range(case):
    col = int(input())
    pascal = []
    for j in range(col+1):
        if j == 0:
            pascal.append([1])
        else:
            pascal.append([])
            for k in range(j+1):
                pascal[j].append(1) if k == 0 or k == j else pascal[j].append(pascal[j-1][k-1]+pascal[j-1][k])
    result = []
    for l in range(col):
        result.append(' '.join(map(str,pascal[l])))
    print('#{}'.format(i+1))
    print('\n'.join(result))