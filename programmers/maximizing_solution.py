def solution(expression):
    answer_list = []
    number =''
    priority_list = [['-', '+', '*'], ['+', '-', '*'], ['*', '-', '+'], ['*', '+', '-'], ['-', '*', '+'], ['+', '*', '-']]
    for priority in priority_list:
        operations = []
        expression_list = []
        for i in expression:
            if(i.isdigit()):
                number += i
            else:
                expression_list.append(int(number))
                number = ''
                while(operations and priority.index(operations[-1]) >= priority.index(i)):
                    b = expression_list.pop()
                    a = expression_list.pop()
                    c = operations.pop()
                    if(c == '+'):
                        expression_list.append(a+b)
                    elif(c == '-'):
                        expression_list.append(a-b)
                    else:
                        expression_list.append(a*b)
                operations.append(i)
        
        expression_list.append(int(number))
        
        while(operations):
            b = expression_list.pop()
            a = expression_list.pop()
            c = operations.pop()
            if(c == '+'):
                expression_list.append(a+b)
            elif(c == '-'):
                expression_list.append(a-b)
            else:
                expression_list.append(a*b)
        number = ''
        answer_list.append(abs(expression_list[0]))
        
    answer = 0    
    for i in answer_list:
        if(i > answer):
            answer = i
    
    return answer
