def solution(number, k):    
    answer = ''
    
    length = len(number)-k
    
    delete = 0
    return_list = []
    
    for i in number:
        if(return_list):
            len_return = len(return_list)
            for j in range(len_return):
                if(delete == k):
                    break
                index = len_return-j-1
                if(return_list[index] < i):
                    return_list.pop()
                    
                    delete += 1
                else:
                    break
                
        return_list.append(i)
    for _ in range(k-delete):
        return_list.pop()
    answer = ''.join(return_list)
    
    return answer
