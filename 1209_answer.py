arr = [list(map(int, input().split())) for _ in range(100)]
Max = 0    #최대값(답)

#행우선 순회
for i in range(100):
    S=0
    for j in range(100):
        S += arr[i][j]
    Max = max(Max, S)

for i in range(100):
    S=0
    for j in range(100):
        S += arr[j][i]
    Max = max(Max, S)

S = 0
for i in range(100):
    S += arr[i][i]
Max = max(Max, S)

S = 0
for i in range(100):
    S += arr[i][99-i]
Max = max(Max, S)