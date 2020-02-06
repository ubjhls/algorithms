def divide(a, b, n):
    global result
    if n == len(man):
        result = min(result, max(stairs(a, 0), stairs(b, 1)))
    else:
        divide(a + [n], b, n + 1)
        divide(a, b + [n], n + 1)


def stairs(choice, i):
    [y, x] = exits[i]
    times = []
    for i in choice:
        times.append(abs(man[i][0] - y) + abs(man[i][1] - x) + 1)
    times.sort()
    l = room[y][x]
    for idx in range(len(times)):
        if idx < 3:
            times[idx] += l
        else:
            if times[idx - 3] > times[idx]:
                times[idx] = times[idx - 3] + l
            else:
                times[idx] += l
    if times:
        return times[-1]
    else:
        return 0


for tc in range(int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    man = []
    exits = []
    result = 10 ** 6
    for y in range(N):
        for x in range(N):
            if room[y][x]:
                if room[y][x] == 1:
                    man.append([y, x])
                else:
                    exits.append([y, x])
    divide([], [], 0)
    print(f'#{tc + 1} {result}')