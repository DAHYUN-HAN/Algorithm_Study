def solution(d, budget):
    answer = 0
    d = sorted(d)
    sum = 0
    for i in d:
        sum += i
        if(sum <= budget):
            answer += 1
        else:
            break
    return answer
