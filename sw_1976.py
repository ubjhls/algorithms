testcase = int(input())
result = []

for i in range(testcase):
    test = list(map(int, input().split()))
    answer_1 = test[0] + test[2]
    answer_2 = test[1] + test[3]
    if answer_1 > 12:
        answer_1 = answer_1 - 12
    elif answer_2 > 60:
        answer_2 = answer_2 - 60
        answer_1 = answer_1 + 1
    result.append(answer_1)
    result.append(answer_2)
print(result)