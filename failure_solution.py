def solution(N, stages):
    answer = []
    stage = [0] * (N+1)
    people = []
    fail = []
    
    for i in stages:
        stage[i-1] += 1
    sum = 0
    for i in stage:
        sum += i
    
    people.append(sum)
    now = 0
    for i in range(1, N):
        now += stage[i-1]
        people.append(sum-now)
    for i in range(len(people)):
        if(people[i] == 0):
            fail.append((i+1, 0))
        else:
            fail.append((i+1, stage[i] / people[i]))
    fail = sorted(fail, key=lambda x: -x[1])
    for i in fail:
        answer.append(i[0])
    return answer
