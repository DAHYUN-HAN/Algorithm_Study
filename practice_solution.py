#수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(n):
        if(i%2 == 0):
            answer = answer + '수'
        else:
            answer = answer + '박'
    return answer
    
#소수 찾기

def solution(n):
    all_number = [True]*(n+1)
    m = int((n+1) ** 0.5)
    for i in range(2, m+1):
        if(all_number[i]):
            for j in range(i+i, n+1, i):
                all_number[j] = False
    
    count = 0
    
    for i in range(2, n+1):
        if(all_number[i]):
            count += 1
    
    answer = count
    return answer

#정수 제곱근 판별

import math

def solution(n):
    sqrt = math.sqrt(n)
    if(sqrt.is_integer()):
        return (sqrt+1)**2
    else:
        return -1
