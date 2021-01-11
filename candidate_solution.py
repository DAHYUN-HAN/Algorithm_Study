from itertools import combinations

def solution(relation):
    list = []
    candidate_list = []
    for i in range(len(relation[0])):
        list.append(i)
        
    for i in range(len(relation[0])):
        for j in combinations(list, i+1):
            check = []
            combination_list = []
            for k in range(len(j)):
                combination_list.append(j[k])
                
            if(check_minimality(combination_list, candidate_list)):
                continue
                            
            for k in relation:
                inner_list = []
                for p in range(len(j)):
                    inner_list.append(k[j[p]])
                if(not inner_list in check):
                    check.append(inner_list)

            if(len(check) == len(relation)):
                candidate_list.append(combination_list)
    return len(candidate_list)


def check_minimality(combination_list, candidate_list):
    for a in range(len(combination_list)):
        for b in combinations(combination_list, a+1):
            new_list = []
            for c in range(len(b)):
                new_list.append(b[c])
                if(new_list in candidate_list):
                    return True
    return False
