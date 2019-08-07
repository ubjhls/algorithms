testcase = int(input())

for k in range(testcase):
    result=[]
    counter = 0
    b= int(input())
    for j in input():
        result.append(int(j))
    for i in range(10):
        if result.count(i) >= counter:
            counter = result.count(i)
            num = i 
    print(f'#{k+1} {num}',counter)
