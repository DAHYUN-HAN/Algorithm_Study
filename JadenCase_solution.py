def solution(s):
    answer = ''
    Upper = True
    for i in s:
        if(i == ' '):
            Upper = True
            answer += ' '
            continue
            
        if(Upper):
            answer += i.upper()
            Upper = False
        else:
            answer += i.lower()
    
    return answer
