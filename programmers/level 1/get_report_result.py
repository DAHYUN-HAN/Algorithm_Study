def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_result = {}
    for string in report :
        user = string.split(" ")[0]
        reported_user = string.split(" ")[1]
        try :
            if(user not in report_result[reported_user]) :
                report_result[reported_user].append(user)
        except :
            report_result[reported_user] = [user]
                
    for key, value in report_result.items():
        if(len(value) >= k) :
            for i in range(len(value)):
                answer[id_list.index(value[i])] += 1
                
    return answer
