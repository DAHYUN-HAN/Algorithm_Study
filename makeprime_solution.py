def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if(i != j and j != k and i != k):
                    if(check(nums[i] + nums[j] + nums[k])):
                        answer +=1
    return answer

def check(number):
    for i in range(3, (number // 2) + 1):
        if(number % i == 0):
            return False
    return True
