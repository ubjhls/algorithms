T = int(input())

arr = [list(map(int, input().split())) for _ in range(T)]

for j in range(T):
    count = 1
    result = ''
    for i in range(T):
        if arr[0][0] < arr[i][0] and arr[0][1] < arr[i][1]:
            count += 1
    result = str(count)
    arr.append(arr[0])
    arr.remove(arr[0])
    print(result,end=' ')