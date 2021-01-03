def solution(record):
    sub_answer = []
    inner_list = []
    name_list = {}
    for i in record:
        str = i.split(' ')
        if(str[0] == 'Enter'):
            inner_list = [str[1], '님이 들어왔습니다.']
            name_list[str[1]] = str[2]
        elif(str[0] == 'Leave'):
            inner_list = [str[1], '님이 나갔습니다.']
        elif(str[0] == 'Change'):
            name_list[str[1]] = str[2]
            continue
        sub_answer.append(inner_list)
    answer = []
    for i in sub_answer:
        answer.append(name_list[i[0]] + i[1])
    return answer
