def solution(people, limit):
    answer = 0
    people = sorted(people, reverse = True)
    last_index = len(people)-1
    for i in range(len(people)):
        if(people[i] + (people[last_index]) > limit):
            answer = answer + 1
        else:
            answer = answer + 1
            last_index = last_index -1
        
        if(last_index <= i):
            break
    return answer
