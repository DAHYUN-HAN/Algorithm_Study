#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def solution(n, stations, w):
    answer = 0
    
    start = 1
    blank_list = []
        
    for i in stations:
        end = i-w-1
        if(start <= end):
            blank_list.append([start, end])
        start = i+w+1
    
    if(start <= n):
        blank_list.append([start, n])
        
    for i in blank_list:
        length = i[1] - i[0] + 1
        if(length <= w*2+1):
            answer += 1
        else:
            answer += math.ceil(length / ((w*2+1)))
    print(blank_list)
        

    return answer

