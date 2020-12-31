def solution(dartResult):
    score_list = [0]
    for i in range(len(dartResult)-1):
        if(dartResult[i].isdigit()):
            if(dartResult[i+1].isdigit()):
                score_list.append(int(dartResult[i:i+2]))
            elif(not dartResult[i-1].isdigit()):
                score_list.append(int(dartResult[i]))
            continue
        check(dartResult[i], score_list)
    check(dartResult[-1], score_list)
    answer = 0
    for i in score_list:
        answer += i
        
    return answer

def check(s, score_list):
    if(s == 'D'):
        score_list[-1] = score_list[-1]**2
    elif(s == 'T'):
        score_list[-1] = score_list[-1]**3
    elif(s == '*'):
        score_list[-2] = score_list[-2]*2
        score_list[-1] = score_list[-1]*2
    elif(s == '#'):
        score_list[-1] = score_list[-1] * (-1)
    return score_list
