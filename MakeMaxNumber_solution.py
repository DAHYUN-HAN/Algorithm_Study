def solution(numbers):
    
    numbers_list = []
    for i in numbers:
        numbers_list.append(str(i)*3)
    numbers_list = sorted(numbers_list, reverse = True)
    answer = ''
    for i in numbers_list:
        length = int(len(i)/3)
        answer = answer + i[:length]
    answer = str(int(answer))
    return answer
