import numpy as np

def solution(answers):
    student_count = [0] * 3
    answer = []
    
    first_answer = [1,2,3,4,5]
    first_count = 0
    second_answer = [2,1,2,3,2,4,2,5]
    second_count = 0
    third_answer = [3,3,1,1,2,2,4,4,5,5]
    third_count = 0
    
    for i in range(len(answers)):
        student = [first_answer[first_count], second_answer[second_count], third_answer[third_count]]
        
        for j in range(len(student)):
            if(answers[i] == student[j]):
                student_count[j] = student_count[j] + 1     
        first_count += 1
        second_count += 1
        third_count += 1
        
        if(first_count == 5):
            first_count = 0
        if(second_count == 8):
            second_count = 0
        if(third_count == 10):
            third_count = 0
                
    max_correct = np.max(student_count)
    for i in range(len(student_count)):
        if(student_count[i] == max_correct):
            answer.append(i+1)
    return answer
