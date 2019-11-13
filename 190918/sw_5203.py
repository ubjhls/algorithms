T = int(input())
for i in range(1, T + 1):
    player_1 = []
    player_2 = []
    card = list(map(int, input().split()))
    result = 0
    for j in range(0, 12, 2):
        player_1.append(card[j])
        player_2.append(card[j + 1])
        if j < 4:
            continue
        for k in range(len(player_1)):
            tmp_1 = player_1[k]
            if len(player_1) >= 3:
                if player_1.count(tmp_1) >= 3:
                    result = 1
                    break
        play_1 = sorted(player_1)
        for k in range(2, len(play_1)):
            temp_1 = play_1[k]
            if (play_1[k] == temp_1 and play_1[k - 1] == temp_1 - 1 and play_1[k - 2] == temp_1 - 2) or (
                    play_1[k] == temp_1 and play_1[k - 1] == temp_1 + 1 and play_1[k - 2] == temp_1 + 2):
                result = 1
                break
        if result != 0:
            break
        for k in range(len(player_2)):
            tmp_2 = player_2[k]
            if len(player_2) >= 3:
                if player_2.count(tmp_2) >= 3:
                    result = 2
                    break
        play_2 = sorted(player_2)
        for k in range(2, len(play_2)):
            temp_2 = play_2[k]
            if (play_2[k] == temp_2 and play_2[k - 1] == temp_2 - 1 and play_2[k - 2] == temp_2 - 2) or (
                    play_2[k] == temp_2 and play_2[k - 1] == temp_2 + 1 and play_2[k - 2] == temp_2 + 2):
                result = 2
                break
        if result != 0:
            break
    print('#{} {}'.format(i, result))