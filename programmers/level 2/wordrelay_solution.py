def solution(n, words):
    now = 2
    count = 1
    word_list = []
    wrong = False
    for i in words:
        if(word_list):
            if(word_list[-1][-1] != i[0]):
                wrong = True
                break
            if(not i in word_list):
                word_list.append(i)
                now += 1
                if(now == n+1):
                    now = 1
                    count += 1
            else:
                wrong = True
                break
        else:
            word_list.append(i)
            
    if(wrong):
        answer = [now, count]
    else:
        answer = [0,0]
    return answer
