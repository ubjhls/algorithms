from itertools import combinations

princess = [input() for _ in range(5)]
tmp = []
arr = []

for i in range(5):
    for j in range(5):
        tmp.append((i, j))

for i in combinations(tmp, 7):
    count = 0
    for j in i:
        x, y = j
        if princess[x][y] == 'S':
            count += 1
    if count >= 4:
        arr.append(i)
