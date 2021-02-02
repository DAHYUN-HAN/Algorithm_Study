import numpy as np
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    finish = []
    now = deque()
    now_time = deque()
    num_truck = len(truck_weights)
    truck_weights = list(reversed(truck_weights))
    count = 0
    while(len(finish) != num_truck):
        count += 1
        if(truck_weights):
            if(np.sum(now)+truck_weights[-1]<=weight):
                now.append(truck_weights.pop())
                now_time.append(0)
        for i in range(len(now_time)):
            now_time[i] += 1
        if(now_time[0] == bridge_length):
            now_time.popleft()
            finish.append(now.popleft())
    answer = count + 1      
    return answer
