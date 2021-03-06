import sys
sys.setrecursionlimit(10**6)
read = lambda : sys.stdin.readline().strip()


def make_group(x, cnt, step):
    # step은 시작정점
    global d, check, s
    # 탐색할수록 정점의 개수(cnt)는 늘어간다.
    # d 배열에 탐색할때마다 해당 정점을 기준으로 탐색된 정점의 개수를 저장한다.

    while True:
        if check[x] != False:
            # 이미 들어간거
            if step != s[x-1]:
                # 이미 방문했고, 정점 시작점이 다를 경우 사이클 x
                return 0
            return cnt - check[x]
            # 그러던 중 사이클이 존재하면, 사이클이 존재하는 정점을 인덱스로 활용하는 것이다.
            # (탐색된 정점 개수 - 사이클 정점에 대한 길이)를 통해 사이클을 이루는 정점의 개수를 구하게 된다.

        check[x] = cnt
        # check는 x에 도착했을 때 탐색한 개수를 저장하는 곳이다.
        s[x-1] = step
        # x가 어디에서 시작했는지를 알려주는 것
        x = d[x]
        # 다음애...
        cnt += 1

for _ in range(int(read())):
    n = int(read())
    check = [False]*(n+1)

    d = {}
    s = list(map(int, read().split()))
    for i in range(1, n+1):
        d[i] = s[i-1]

    ans = 0
    for i in d:
        if check[i] == False:
            ans += make_group(i, 1, i);

    print(n-ans)