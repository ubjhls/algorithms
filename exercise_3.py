def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        result = [tree.find(s) if s in tree else -1 for s in skill]
        flag1, flag2 = True, True
        print(result)
        for idx in range(len(result)):
            if flag1:
                if result[idx] == -1:
                    flag1 = False
                else:
                    if idx != len(result)-1:
                        if result[idx+1] == -1:
                            continue
                        elif result[idx] > result[idx+1]:
                            flag2 = False
                            break
            else:
                if result[idx] != -1:
                    flag2 = False
                    break
        answer += 1 if flag2 else 0           
    return answer