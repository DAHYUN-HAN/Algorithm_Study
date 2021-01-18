def solution(numbers, hand):
    answer = ''
    
    now_L = [3,0]
    now_R = [3,2]
    
    for i in numbers:
        if(i % 3 == 1):
            answer += 'L'
            now_L = [i//3,0]
        elif(i != 0 and i % 3 == 0):
            answer += 'R'
            now_R = [i//3 -1,2]
            
        else:
            if(i == 0):
                want = [3,1]
            elif(i % 3 == 2):
                want = [i//3,1]
                
            L_distance = calc(want, now_L)
            R_distance = calc(want, now_R)
            if(L_distance < R_distance):
                answer += 'L'
                now_L = want
            elif(L_distance == R_distance):
                if(hand == 'left'):
                    answer += 'L'
                    now_L = want
                else:
                    answer  += 'R'
                    now_R = want
            else:
                answer += 'R'
                now_R = want
    return answer


def calc(want, now):
    distance = abs(want[0]-now[0]) + abs(want[1]-now[1])
    return distance
