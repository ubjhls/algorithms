def check_size(i, j, size):
    for a in range(size):
        for b in range(size):
            tmp_i = i + a
            tmp_j = j + b
            if 0 <= tmp_i <= 9 and 0 <= tmp_j <= 9:
                if not(paper[tmp_i][tmp_j]):
                    return False
            else:
                return False
    return True

def remove_paper(i, j, size):
    global cnt
    for a in range(size):
        for b in range(size):
            paper[i+a][j+b] = 0
            cnt -= 1

def revive_paper(i, j, size):
    global cnt
    for a in range(size):
        for b in range(size):
            paper[i+a][j+b] = 1
            cnt += 1

def backtracking(i, j, size_cnt, k):
    global min_k
    if cnt == 0 and size_cnt[0] > -1 and size_cnt[1] > -1 and size_cnt[2] > -1 and size_cnt[3] > -1 and size_cnt[4] > -1:
        if min_k > k:
            min_k = k
    elif size_cnt[0] < 0 or size_cnt[1] < 0 or size_cnt[2] < 0 or size_cnt[3] < 0 or size_cnt[4] < 0:
        pass
    else:
        while i < 10:
            while j < 10:
                if paper[i][j]:
                    for size in range(5, 0, -1):
                        if check_size(i, j, size):
                            size_cnt[size-1] -= 1
                            remove_paper(i, j, size)
                            backtracking(i, j+size, size_cnt, k+1)
                            size_cnt[size-1] += 1
                            revive_paper(i, j, size)
                if paper[i][j]:
                    return
                j += 1
            j = 0
            i += 1

paper = []
cnt = 0
min_k = 25
for _ in range(10):
    data = list(map(int, input().split()))
    paper.append(data)
    for e in data:
        if e:
            cnt += 1
if cnt:
    backtracking(0, 0, [5,5,5,5,5], 0)
    if min_k == 25:
        print(-1)
    else:
        print(min_k)
else:
    print(0)