for w in range(int(input())):
    pattern = input()
    string = input()
    for j in range(len(string)-len(pattern)):
        count = 0
        if pattern[0] == string[j]:
            for k in range(len(pattern)):
                if pattern[0+k] == string[j+k]:
                    count += 1
                else:
                    break
            if count == len(pattern):
                print('#{} {}'.format(w + 1, 1))
                break
        if count != len(pattern):
            print('#{} {}'.format(w + 1, 0))
            break