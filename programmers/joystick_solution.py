def solution(name):
    change = 0
    count = 0
    first_count = 0
    temp_count = 0
    first_move = len(name)-1
    second_move = len(name)-1
    is_continuity = True
    is_start = True
    start = 100
    end = 100
    for i in range(len(name)):
        if(i > 0):
            if(name[i] == 'A'):
                if(is_continuity):
                    first_count +=1
                temp_count += 1
                if(is_start):
                    temp_start = i
                    is_start = False
            else:
                is_continuity = False
                if(count < temp_count):
                    count = temp_count
                    temp_count = 0
                    start = temp_start-1
                    is_start = True
                    end = i-1
                
        if(name[i] < 'N'):
            change += ord(name[i])-65
        else:
            change += 91-ord(name[i])

    first_move -= first_count
    second_move = start*2 + second_move- end
    if(first_move < second_move):
        move = first_move
    else:
        move = second_move
    answer = change+move
    return answer
