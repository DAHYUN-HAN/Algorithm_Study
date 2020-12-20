def solution(numbers):
    answer_list = []
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            is_input = True
            sum = numbers[i] + numbers[j+i+1]
            if answer_list:
                for answer in answer_list:
                    if(answer == sum):
                        is_input = False
                if(is_input):
                    answer_list.append(sum)
            else:
                answer_list.append(sum)
    answer = sorted(answer_list)
    return answer
