def solution(s):
    tmp = [[] for _ in range(s.count(' ')+1)]
    count = 0
    result = ''
    for i in range(s.count(' ') + 1):
        for j in range(len(s) + 1):
            if ord(s[count]) == 32:
                count += 1
                break
            tmp[i].append(s[count])
            if count == len(s)-1:
                break
            count += 1
    for i in range(s.count(' ') + 1):
        for idx,value in enumerate(tmp[i]):
            if idx % 2 == 0:
                result += value.upper()
            else:
                result += value.lower()
        if i < s.count(' '):
            result += ' '
    return result
print(solution(' asd etwerf'))