def solution(skill, skill_trees):
    answer = 0
    length = len(skill)
    for i in skill_trees:
        bool_skill = [False]*length
        check = True
        for j in i:
            if(j in skill):
                for k in range(length):
                    if(j == skill[k]):
                        bool_skill[k] = True
                        break
                    else:
                        if(not bool_skill[k]):
                            check = False
                            break
            if(not check):
                break
        if(check):
            answer += 1
    return answer
