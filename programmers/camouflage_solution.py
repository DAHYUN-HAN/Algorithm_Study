def solution(clothes):
    answer = 1
    case= {}
    for i in clothes:
        if(not i[1] in case):
            case[i[1]] = 1
        else:
            case[i[1]] += 1
            
    for i in case:
        answer  = answer * (case[i]+1)
    answer -= 1
    return answer
