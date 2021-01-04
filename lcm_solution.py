def solution(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        b = arr[i]
        a = LCM(a, b)
        
    return a

def LCM(a, b):
    if(a > b):
        big = a
        small = b
    else:
        big = b
        small = a
    while(small != 0):
        n = big%small
        big = small
        small = n
    return (a*b / big)
