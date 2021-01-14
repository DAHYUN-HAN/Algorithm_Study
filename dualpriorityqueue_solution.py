def solution(operations):
    answer = []
    list = []
    
    for i in operations:
        operation = i.split(' ')
        if(operation[0] == 'I'):
            list.append(int(operation[-1]))
            list = sorted(list)
        elif(operation[-1] == '1'):
            if(list):
                list.pop()
        elif(operation[-1] == '-1'):
            if(list):
                del list[0]
    if(list):
        return[list[-1], list[0]]
    else:
        return [0,0]
