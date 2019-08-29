testcase = int(input())

for i in range(testcase):
    num = list(map(int,input().split()))

    rotate = list(map(int, input().split()))

    for j in range(num[1]):
        tmp = rotate.pop(0)
        rotate.append(tmp)
    print('#{} {}'.format(i+1, rotate[0]))