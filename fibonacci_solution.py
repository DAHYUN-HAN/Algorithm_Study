def solution(n):
    fibonacci = [0,1]
    for i in range(2, n+1):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    answer = fibonacci[-1] % 1234567
    return answer
