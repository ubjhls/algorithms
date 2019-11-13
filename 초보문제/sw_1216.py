for i in range(10):
    n = input()
    string = [input() for i in range(100)]
    result = 0

    for j in range(100):
        for w in range(2, 101):
            if result <  w:
                for k in range(101 - w):
                    text = ''
                    text += string[j][k:k + w]
                    if text == text[::-1]:
                        result = w
                        break

    for j in range(100):
        for w in range(2, 101):
            if result < w:
                for k in range(101 - w):
                    text = ''
                    for q in range(k, k + w):
                        text += string[q][j]
                    if text == text[::-1]:
                        result = w
                        break
    print('#{} {}'.format(n, result))
