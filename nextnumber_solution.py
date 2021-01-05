def solution(n):
    n_list = []
    while(n != 0):
        n_list.append(n%2)
        n = n//2
    print(n_list)
    first_change = False
    second_change = False
    index = len(n_list)
    for i in range(1, len(n_list)):
        if(n_list[i] == 0 and n_list[i-1] == 1):
            n_list[i] = 1
            n_list[i-1] = 0
            index = i-1
            first_change = True
            break
            
    if(not first_change):
        n_list.pop()
        n_list.append(0)
        n_list.append(1)
    if(n_list[0] == 0):
        for i in range(index):
            if(n_list[i]==1):
                new_index = i
                second_change = True
        if(second_change):
            n_list[0] = 1
            n_list[new_index] = 0
        
    answer = 0
    for i in range(len(n_list)):
        answer += n_list[i] * (2**i)

    return answer

