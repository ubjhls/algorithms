testcase = int(input())

for i in range(testcase):
    test = int(input())
    vel = [list(map(int, input().split())) for j in range(test)]
    result = 0
    answer = 0
    for j in range(test):
        if vel[j][0] == 1:
            result += vel[j][1]
            answer += result
        elif vel[j][0] == 2:
            if result <vel[j][1]:
                result = 0
            else:
                result -= vel[j][1]
            answer += result
        elif vel[j][0] == 0:
            answer += result
    print('#{} {}'.format(i+1, answer))