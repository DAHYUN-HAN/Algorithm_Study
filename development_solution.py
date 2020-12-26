import math

def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    now = days[0]
    count = 0
    
    for i in days:
        if(now >= i):
            count += 1
        else:
            now = i
            answer.append(count)
            count = 1
    
    answer.append(count)
    return answer
