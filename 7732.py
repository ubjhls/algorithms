testcase =int(input())

test = list(map,int(input().split()))
result= []
count = 1
for i in range(test[0]):
    for j in range(test[1]):
        result[i][j].append(count)
        count += 1

for i in range(test[0]):