def solution(files):
    answer = []
    split_files = []
    for i in range(len(files)):
        check_head = True
        check_number = True
        head = ''
        number =''
        tail = ''
    
        for j in files[i]:
            if(check_head):
                if(not j.isdigit()):
                    head += j
                else:
                    check_head = False
                    number += j
            elif(check_number):
                if(j.isdigit()):
                    number += j
                else:
                    check_number = False
                    tail += j
            else:
                tail += j
        split_files.append([head.lower(), int(number), tail, i])       
        
    split_files = sorted(split_files, key = lambda x:(x[0], x[1]))
    
    for i in split_files:
        answer.append(files[i[-1]])
    return answer
