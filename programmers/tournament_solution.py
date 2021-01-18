def solution(n,a,b):
    answer = 1
    
    if(a<b):
        left = a
        right = b
    else:
        left = b
        right = a
        
    while(True):
        if(left%2 == 1 and right%2 == 0 and right == left+1):
            return answer
        else:
            right = round(right / 2 + 0.1)
            left = round(left / 2 + 0.1)
            answer += 1
            print(right, left)
