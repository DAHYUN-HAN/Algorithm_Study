def solution(n):
    answer = []
    n_sum = 0
    for i in range(1, n+1):
        answer.append([0]*(i))
        n_sum += i
    
    l_index = n-1
    start_r_index = 0
    end_r_index = -1
    l_min = 0
    l_max = n
    r_min = 1
    r_max = n
    k=1
    is_finish = False
    while(not is_finish):
        answer, k, is_finish =down(answer, l_min, l_max, start_r_index, k, n_sum, is_finish)
        start_r_index +=1
        l_min +=1
        l_max -=1
        answer, k, is_finish = right(answer, r_min, r_max, l_index, k, n_sum, is_finish)
        r_min +=1
        l_index -=1
        r_max -=1
        answer, k, is_finish = up(answer, l_min, l_max, end_r_index, k, n_sum, is_finish)
        l_min +=1
        r_max -=1
        end_r_index -=1
    
    answer = sum(answer, [])
        
    return answer

def down(answer, l_min, l_max, r_index, k, n_sum, is_finish):
    for i in range(l_min, l_max):
        
        answer[i][r_index] = k
        k += 1
        if(k > n_sum):
            is_finish = True
            break
    return answer, k, is_finish

def right(answer, r_min, r_max, l_index, k, n_sum, is_finish):
    for i in range(r_min, r_max):
        
        answer[l_index][i] = k
        k += 1
        if(k > n_sum):
            is_finish = True
            break
    return answer, k, is_finish

def up(answer, l_min, l_max, r_index, k, n_sum, is_finish):
    for i in range(l_max, l_min, -1):
        
        answer[i-1][r_index] = k
        k += 1
        if(k > n_sum):
            is_finish = True
            break
    return answer, k, is_finish
