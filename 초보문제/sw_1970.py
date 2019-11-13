testcase = int(input())

for i in range(testcase):
    print('#{}'.format(i+1))
    count_50000 = 0
    count_10000 = 0
    count_5000 = 0
    count_1000 = 0
    count_500 = 0
    count_100 = 0
    count_50 = 0
    count_10 = 0
    money = int(input())
    if money >= 50000:
        count_50000 = money // 50000
        money = money % 50000
    if money >= 10000:
        count_10000 = money // 10000
        money = money % 10000
    if money >= 5000:
        count_5000 = money // 5000
        money = money % 5000
    if money >= 1000:
        count_1000 = money // 1000
        money = money % 1000
    if money >= 500:
        count_500 = money // 500
        money = money % 500
    if money >= 100:
        count_100 = money // 100
        money = money % 100
    if money >= 50:
        count_50 = money // 50
        money = money % 50
    if money >= 10:
        count_10 = money // 10
    print('{} {} {} {} {} {} {} {}'.format(count_50000,count_10000,count_5000,count_1000,count_500,count_100,count_50,count_10))