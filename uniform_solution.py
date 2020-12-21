def solution(n, lost, reserve):
    student = [1]*n
    
    for i in range(len(lost)):
        student[lost[i]-1] -= 1
        
    for i in range(len(reserve)):
        student[reserve[i]-1] += 1
        
    sum = 0
    for i in range(len(student)-1):
        if(student[i] == 0 and student[i+1] == 2):
            student[i] = 1
            student[i+1] = 1
    
    for i in range(1,len(student)):
        if(student[i] == 0 and student[i-1] == 2):
            student[i] = 1
            student[i-1] = 1
            
    for i in student:
        if(i != 0):
            sum += 1
    answer = sum
    return answer
