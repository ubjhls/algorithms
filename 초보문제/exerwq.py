for T in range(1, int(input())+1):
    command = input()
    S = [0]*13
    D = [0]*13
    H = [0]*13
    C = [0]*13
    flag = True
    for idx in range(0, len(command), 3):
        card = command[idx]
        number = int(command[idx+1:idx+3]) - 1
        if card == 'S':
            if not S[number]:
                S[number] = 1
            else:
                flag = False
                break
        elif card == 'D':
            if not D[number]:
                D[number] = 1
            else:
                flag = False
                break
        elif card == 'H':
            if not H[number]:
                H[number] = 1
            else:
                flag = False
                break
        else:
            if not C[number]:
                C[number] = 1
            else:
                flag = False
                break
    print('#{} {} {} {} {}'.format(T, S.count(0), D.count(0), H.count(0), C.count(0))) if flag else print('#{} ERROR'.format(T))