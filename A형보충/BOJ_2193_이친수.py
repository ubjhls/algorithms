x = int(input())

def dp(x):
    dpl = [1, 1]
    if(x==1 or x==2):
        return 1
    for i in range(2,x):
        dpl.append(dpl[i-1]+dpl[i-2])
    return dpl[x-1]

print(dp(x))