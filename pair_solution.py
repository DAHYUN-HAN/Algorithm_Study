def solution(s):
    s_list = [0]
    for i in s:
        if(s_list[-1] == i):
            s_list.pop()
        else:
            s_list.append(i)
    
    if(len(s_list) == 1):
        answer = 1
    else:
        answer = 0
    return answer
