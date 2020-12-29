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
    
#2016년
def solution(a, b):
    day = 0
    for i in range(1, a):
        if(i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i== 10 or i ==12):
            day += 31
        elif(i == 2):
            day += 29
        elif(i == 4 or i == 6 or i == 9 or i == 11):
            day += 30
    day += b
    day = day % 7
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[day]
