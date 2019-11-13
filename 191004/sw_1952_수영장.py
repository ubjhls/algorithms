def dfs(money, month):
    global result
    if month > 11:
        result.append(money)
        return
    if plan[month] == 0:
        dfs(money, month + 1)
    dfs(money + plan[month] * cost[0], month + 1)
    dfs(money + cost[1], month + 1)
    dfs(money + cost[2], month + 3)


T = int(input())
for t in range(1, T + 1):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    money = 0
    result = []
    result.append(cost[3])
    dfs(0, 0)
    print('#{} {}'.format(t, min(result)))