testcase = int(input())
for k in range(testcase):
    b= int(input())
    a = list(map(int, input().split()))
    tmp = max(a)-min(a)

    print(f'#{k+1} {tmp}')