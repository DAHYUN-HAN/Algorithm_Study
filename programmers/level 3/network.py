def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(graph, v, visited):
        visited[v] = True
        for i in range(len(graph[0])):
            if(graph[v][i] == 1):
                if(not visited[i]):
                    dfs(graph, i, visited)
                    
    while(True):
        finish = True
        for check in range(len(visited)):
            if(not visited[check]):
                finish = False
                dfs(computers, check, visited)
                answer += 1
        if(finish):
            break
            
    return answer
    
