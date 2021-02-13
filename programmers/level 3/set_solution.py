def solution(n, s):
    answer = []
    if(s < n):
        return [-1]
    number = s / n
    
    for i in range(n):
        answer.append(int(number))
        
    if not(number.is_integer()):
        k = -1
        for i in range(s % n):
            answer[k] += 1
            k -= 1
    return answer
