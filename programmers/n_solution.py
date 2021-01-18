Alpha = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def solution(n, t, m, p):
    answer = ''
    now = 0
    number = ''
    while(len(number) < t*m):
        number  = number+ ''.join(get_number(n, now))
        now += 1
    if(m == p):
        p = 0
    for i in range(len(number)):
        if((i+1) % m == p):
            answer += number[i]
        if(len(answer) == t):
            break
    return answer

def get_number(n, number):
    number_list = []
    if(number == 0):
        return ['0']
    while(number != 0):
        temp = number % n
        if(temp < 10):
            number_list.append(str(temp))
        else:
            number_list.append(Alpha[temp])
        number = number // n
    number_list.reverse()
    return number_list
