import numpy as np

def solution(s):
    length = len(s)
    amount = int(len(s)/2)
    answer_list = []
    
    if(length == 1):
        return 1
    
    for i in range(amount):
        split = i+1
        s_list = []
        count_list = []
        count = 1
        for j in range(length // split):
            word = s[j*split:j*split+split]
            if(s_list):
                if(s_list[-1] != word):
                    if(count != 1):
                        count_list.append(count)
                    s_list.append(word)
                    count = 1
                else:
                    count += 1
            else:
                s_list.append(word)
        if(count != 1):        
            count_list.append(count)
            
        number_string = ''
        for i in count_list:
            number_string = number_string + str(i)
        len_answer = len(number_string) + len(s_list)*split + (length % split)
        answer_list.append(len_answer)
    
    answer = int(np.min(answer_list))
    return answer
