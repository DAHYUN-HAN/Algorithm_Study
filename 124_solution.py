def solution(n):
    answer = ''
    answer_list = []
    q = n
    while(True):
        q = q-1
        r = q%3+1
        q = int(q/3)
        
        if(r == 3):
            r = 4
        answer_list.append(r)
        if(q == 0):
            break
    answer_list = reversed(answer_list)
    answer = "".join(map(str, answer_list))
    return answer
