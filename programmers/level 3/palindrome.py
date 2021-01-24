def solution(s):
    answer = 0
    
    for i in range(len(s)):
        word = ''
        for j in range(len(s), i, -1):
            word = s[i:j]
            check = True
            
            if(len(word) < answer):
                continue
            for k in range(len(word)):
                if(word[k] != word[len(word)-k-1]):
                    check = False
                    break
            if(check):
                if(answer < len(word)):
                    answer = len(word)
                    break
    return answer
