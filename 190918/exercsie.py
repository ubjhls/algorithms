a =[1,2,3]
n = len(a)
for i in range(1<<n):
    tmp = []
    for j in range(n):
        if i & (1<<j):
            tmp.append(a[j])
    print(tmp)