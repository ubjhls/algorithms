N = int(input())
choo = list(map(int, input().split()))
N1 = int(input())
check = list(map(int, input().split()))

visited = [False]*(sum(choo)+1)
visited[0] = True
for s in choo:
    for i, e in enumerate(visited[:]):
        if e:
            if not(visited[i+s]):
                visited[i+s] = True

for s in choo:
    for i, e in enumerate(visited[:]):
        if e:
            if i-s >= 0:
                if not(visited[i-s]):
                    visited[i-s] = True

for c in check:
    if c > len(visited)-1:
        print("N", end=" ")
    else:
        if visited[c]:
            print("Y", end=" ")
        else:
            print("N", end=" ")