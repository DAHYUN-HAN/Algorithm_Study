def solution(routes):
    answer = 0
    routes = sorted(routes)
            
    out = routes[0][1]
    for i in range(1, len(routes)):

        if(out < routes[i][0]):
            answer += 1
            out = routes[i][1]
        if(out >= routes[i][1]):
            out = routes[i][1]
            
    return answer+1
