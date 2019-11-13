testcase = int(input())

for i in range(testcase):
    book = list(map(int, input().split()))
    count_1 = 0
    while 1:
        tmp = 0
        if book[1]<book[0]:
            tmp = book[0]/2
            count_1 += 1
        elif book[1]>book[0]:
            tmp = book[1]/2
            count_1 += 1
        elif tmp == book[1]:
            result_1 = (book[1])
            break
    count_2 = 0
    while 1:
        tmp = 0
        if book[2]<book[0]:
            tmp = book[0]/2
            count_2 += 1
        elif book[2]>book[0]:
            tmp = book[2]/2
            count_2 += 1
        elif tmp == book[2]:
            result_2 = (book[2])
            break
    if count_1 < count_2:
        print('#{} {}'.format(i+1,'A'))
    elif count_1 > count_2:
        print('#{} {}'.format(i+1,'B'))
    else:
        print(0)