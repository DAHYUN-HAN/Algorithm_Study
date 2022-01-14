import math

def solution(fees, records):
    answer = []
    record_dic = {}
    final_time = 23*60 + 59
    for info in records:
        time, car, check = info.split(" ")
        hour, minute = time.split(":")
        minute_time = int(hour) *60 + int(minute)
        
        if(record_dic.get(car) == None) :
            record_dic[car] = [minute_time]
        else :
            record_dic[car].append(minute_time)
    record_dic = dict(sorted(record_dic.items()))
    
    for key, value in record_dic.items():
        if(len(value) % 2 == 1) :
            record_dic[key].append(final_time)
        sum_time = 0
        for i in range(0, len(value), 2):
            sum_time += value[i+1] - value[i]
        answer.append(sum_time)
    
    for i in range(len(answer)):
        if(answer[i] <= fees[0]) :
            answer[i] = fees[1]
        else :
            plus_time = answer[i]-fees[0]
            answer[i] = fees[1] + math.ceil(plus_time/fees[2]) * fees[3]
    return answer
