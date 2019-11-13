T = int(input())

for i in range(T):
    num = int(input())
    result = []
    for j in range(num):
        if j == 0 or j == 1 or j==2:
            result.append(1)
        else:
            result.append(result[j-2]+result[j-3])
    print(result[j])