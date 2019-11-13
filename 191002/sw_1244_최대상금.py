r = range
for T in r(int(input())):
    N, M = input().split()
    a = [N]
    for i in r(int(M)):
        b = a
        a = []
        for A in r(len(N) - 1):
            for B in r(A + 1, len(N)):
                for x in r(len(b)):
                    c = b[x]
                    c = c[:A] + c[B] + c[A + 1:B] + c[A] + c[B + 1:]
                    if c not in a:
                        a += [c]

    print("#{} {}".format(T + 1, max(map(int, a))))