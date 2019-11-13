def profit(service_center, service_size):
    profit_tmp, receiver = -(service_size ** 2 + (service_size - 1) ** 2), 0
    for house in result:
        distance = abs(house[0] - service_center[0]) + abs(house[1] - service_center[1]) + 1
        if distance <= service_size:
            profit_tmp += cost
            receiver += 1
    if profit_tmp >= 0:
        return receiver
    else:
        return 0
def solution(size):
    global answer
    answer = -1
    for service_size in range(1, size * 2):
        for i in range(size):
            for j in range(size):
                answer = max(answer, profit((i, j), service_size))

    return answer

T = int(input())
for t in range(1, T + 1):
    size, cost = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(size)]
    result = []
    for i in range(size):
        for j in range(size):
            if city_map[i][j]:
                result.append((i, j))

    answer = solution(size)
    print('#{} {}'.format(t, answer))
