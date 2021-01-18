def solution(p):
    
    answer = check(p)
        
    return answer

def check(w):
    if(w == ''):
        return ''
    num_open = 0
    num_close = 0
    u = ''
    v = ''
    is_u = False
    for i in w:
        if(not is_u):
            if(i == '('):
                num_open += 1
            else:
                num_close += 1

            u += i
            if(num_open == num_close):
                is_u = True
        else:
            v += i
    if(u[0] == '('):
        return u+check(v)
    else:            
        new_u = ''
        for i in range(1, len(u)-1):
            if(u[i] == '('):
                new_u += ')'
            else:
                new_u += '('
        return '('+check(v) + ')'+new_u
