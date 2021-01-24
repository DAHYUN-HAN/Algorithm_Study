def solution(dirs):
    answer = 0
    x = 0
    y = 0
    
    way_list = []
    
    for i in dirs:
        if(i == 'U'):
            x2 = x
            y2 = y+1
        elif(i == 'D'):
            x2 = x
            y2 = y-1
        elif(i == 'R'):
            x2 = x+1
            y2 = y
        elif(i == 'L'):
            x2 = x-1
            y2 = y
        
        if not (x2 < -5 or x2 > 5 or y2 < -5 or y2 > 5):
            way = [x, y, x2, y2]
            way2 = [x2, y2, x, y]
            if(not way in way_list):
                way_list.append(way)
                way_list.append(way2)
                answer += 1
            x = x2
            y = y2
        
    return answer
