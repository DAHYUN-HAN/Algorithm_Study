def solution(triangle):
    dp = [0] * (len(triangle) +1)
    
    now = 0
    dp[0] = triangle[0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if(j == 0):
                triangle[i][j] += triangle[i-1][j]
            elif(j == len(triangle[i])-1):
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])
