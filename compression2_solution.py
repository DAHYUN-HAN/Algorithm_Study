def solution(msg):
    answer = []
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    length = len(msg)
    i = 0
    while(i < length):
        j = i
        while(True):
            if(msg[i:j+1] in dictionary):
                j += 1
            else:
                dictionary.append(msg[i:j+1])
                break
            if(j == length):
                break
        
        answer.append(dictionary.index(msg[i:j])+1)
        i = j
    return answer
