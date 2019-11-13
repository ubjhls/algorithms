def back(count, x, y, result):
    global ans
    if count == num:
        ans = result + abs(x - location[0]) + abs(y - location[1])
        tmp.append(ans)
        return
    ans = result
    for j in range(num):
        if not visit[j]:
            visit[j] = True
            back(count + 1, client[j][0], client[j][1],  result + abs(client[j][0] - x) + abs(client[j][1] - y))
            visit[j] = False

T = int(input())
for t in range(1, T + 1):
    num = int(input())
    location = list(map(int, input().split()))
    client = []
    ans = 0
    tmp = []
    visit = [False] * num
    for i in range(4, len(location), 2):
        client.append((location[i], location[i+1]))
    back(0, location[2], location[3], 0)
    print('#{} {}'.format(t, min(tmp)))