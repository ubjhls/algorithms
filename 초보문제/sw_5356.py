T = int(input())

for i in range(T):
    word = [input() for _ in range(5)]
    tmp = []
    for j in range(5):
        tmp.append(len(word[j]))
    num_max = int(max(tmp))
    result = ''
    for j in range(5):
        if len(word[j]) < num_max:
            for k in range(num_max - len(word[j])):
                word[j] += '@'
    for j in range(num_max):
        for k in range(5):
            if word[k][j] != '@':
                result += word[k][j]
    print('#{} {}'.format(i+1, result))
