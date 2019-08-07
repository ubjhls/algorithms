testcase = int(input())

for k in range(testcase):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = []
    for i in range(len(b)-a[1]+1):
        summ=0
        summ = sum(b[i:i+a[1]])
        result.append(summ)
        
    tmp = max(result) - min(result)
    print(f'#{k+1} {tmp}')