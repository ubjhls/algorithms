T = int(input())

for i in range(T):
    word = input()
    count = 0
    while True:
        if word[count] == word[count+1]:
            word = word[0:count] + word[count+2:len(word)+1]
            count = 0
            if count+1 > len(word):
                count = 0
        count += 1
        if count == len(word) or count == len(word)-1:
            break
    print('#{} {}'.format(i+1,len(word)))