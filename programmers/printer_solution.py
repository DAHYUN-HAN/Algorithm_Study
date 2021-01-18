def solution(priorities, location):
    print_list = []
    wait_list = []
    for i in range(len(priorities)):
        wait_list.append(i)
    count = len(priorities)    
    while(len(print_list) != count):
        now = priorities[0]
        start_print = True
        for i in priorities:
            if(i > now):
                start_print = False
                temp = priorities[0]
                priorities = priorities[1:]
                priorities.append(temp)
                temp = wait_list[0]
                wait_list = wait_list[1:]
                wait_list.append(temp)
                break
        if(start_print):
            print_list.append(wait_list[0])
            if(wait_list):
                wait_list = wait_list[1:]
                priorities = priorities[1:]
                
    for i in range(len(print_list)):
        if(print_list[i] == location):
            answer = i+1
    return answer
