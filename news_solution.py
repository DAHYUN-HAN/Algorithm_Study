def solution(str1, str2):
    answer = 0
    str1_set = make_set(str1)
    str2_set = make_set(str2)
    
    intersection_set = intersection(str1_set, str2_set)
    sum_set = len(str1_set) + len(str2_set) - intersection_set
    if(sum_set == 0):
        return 65536
    answer = int(intersection_set/sum_set * 65536)
    return answer

def make_set(str):
    set_list = []
    for i in range(len(str) -1):
        if(str[i].isalpha() and str[i+1].isalpha()):
            set_list.append(str[i:i+2].lower())
    return set_list

def intersection(str1_set, str2_set):
    intersection_set = []
    if(len(str1_set) < len(str2_set)):
        set1 = str1_set
        set2 = str2_set
    else:
        set1 = str2_set
        set2 = str1_set
    for i in set2:
        for j in range(len(set1)):
            if(i == set1[j]):
                intersection_set.append(i)
                set1[j] = 0
                break
    return len(intersection_set)
