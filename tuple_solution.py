def solution(s):
    s = s[1:-1]
    is_open = False
    s_list = {}
    inner_list = []
    number = ''
    for i in s:            
        if(i == '{'):
            is_open = True
            continue
        elif(i == '}'):
            inner_list.append(number)
            s_list[len(inner_list)] = inner_list
            number = ''
            inner_list = []
            is_open = False
            continue
        if(is_open):
            if(i == ','):
                inner_list.append(number)
                number = ''
            else:
                number += i
    answer = []
    for i in range(len(s_list)):
        for k in s_list[i+1]:
            if(not int(k) in answer):
                answer.append(int(k))
                break
    
    return answer
