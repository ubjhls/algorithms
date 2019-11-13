TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Mat_Weight = list(map(int, input().split()))
    Truck_Weight = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        result = 0
        for unit_Weight in Mat_Weight:
            if Truck_Weight[i] >= unit_Weight and unit_Weight >= result:
                result = unit_Weight
        if result != 0:
            Mat_Weight.remove(result)
        ans += result

    print('#{} {}'.format(tc, ans))