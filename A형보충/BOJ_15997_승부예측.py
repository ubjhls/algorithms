n = input().split()
# print(n)

l = []
q = []
for i in range(6):
    a, b, w, d, l = input().split()
    a = n.index(a)
    b = n.index(b)
    w = float(w)
    d = float(d)
    l = float(l)
    if i == 0:
        score = [0, 0, 0, 0, 0]
        if w != 0:
            score[4] = w
            score[a] = 3
            q.append(score)
        if d != 0:
            score = [0, 0, 0, 0, 0]
            score[4] = d
            score[a] = 1
            score[b] = 1
            q.append(score)
        if l != 0:           
            score = [0, 0, 0, 0, 0]
            score[4] = l
            score[b] = 3
            q.append(score)
    else:
        n_q = []
        for s in q:
            if w != 0:
                score = s.copy()
                score[a] += 3
                score[4] *= w
                n_q.append(score)
            if d != 0:
                score = s.copy()
                score[a] += 1
                score[b] += 1
                score[4] *= d
                n_q.append(score)
            if l != 0:
                score = s.copy()
                score[b] += 3
                score[4] *= l
                n_q.append(score)
        q = n_q

# print(q)
prob = [.0, .0, .0, .0]
for s in q:
    p = s[4]
    m1 = max(s[:4])
    r1 = [i for i, j in enumerate(s[:4]) if j == m1]
    c = len(r1)
    if c <= 2:
        for r in r1:
            prob[r] += p
            s[r] = -1
    else:
        for r in r1:
            prob[r] += ((p * 2) / c)
            s[r] = -1
    # print(r1, prob, s)
    if c < 2:
        m2 = max(s[:4])
        r2 = [i for i, j in enumerate(s[:4]) if j == m2]
        c = len(r2)
        for r in r2:
            prob[r] += (p / c)
for p in prob:
    print(p)