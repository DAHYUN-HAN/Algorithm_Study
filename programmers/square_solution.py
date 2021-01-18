def solution(w,h):
    if(w>h):
        a = w
        b = h
    else:
        a = h
        b = w
    w = b
    h = a
    n = 1
    while(n):
        n = a%b
        a = b
        b = n
    small_w = w/a
    small_h = h/a
    minus = a*((2*small_w)+(small_h-small_w-1))
    
    answer = (w*h)-minus
    return answer
