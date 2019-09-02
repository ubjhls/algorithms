T = list(map(int, input().split()))
num = list(map(int, input().split()))
result = []
for i in range(0,T[0]-2):
    for j in range(1,T[0]-1):
        for k in range(2,T[0]):
            if num[i]+num[j]+num[k] > T[1]:
                continue
            temp = num[i]+num[j]+num[k] - T[1]
            temp = -1 * temp
            result.append(temp)
print(min(result)+T[1])