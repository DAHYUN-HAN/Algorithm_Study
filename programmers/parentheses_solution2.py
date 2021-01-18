def solution(s):    
    s_list = []
    for i in s:
        if(not s_list):
            s_list.append(i)
            continue
        if(i == ')'):
            check = s_list.pop()
            if(check != '('):
                return False
        else:
            s_list.append(i)
    if(s_list):
        answer = False
    else:
        answer = True

    return answer
