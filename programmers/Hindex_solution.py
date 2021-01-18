def solution(citations):
    citations = sorted(citations, reverse = True)
    answer = len(citations)
    for i in range(len(citations)):
        if(i+1 > citations[i]):
            answer = i
            break
    
    return answer
