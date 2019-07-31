

def view(arr):
    count=0
    for i in range(2, len(arr)-2):
        building = arr[i]
        left = max(arr[i-2:i])
        if building < left:
            continue
        right = max(arr[i+1:i+3])
        if building < right:
            continue
        building_tmp = max(left,right)
        count += building-building_tmp
    return count

testcase = int(input())
for j in range(10):
    a = list(map(int, input().split()))
    print(f'#{j+1} {view(a)}')