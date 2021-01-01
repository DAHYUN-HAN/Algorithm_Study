#수박수박수박수박수박수?
def solution(n):
    answer = ''
    for i in range(n):
        if(i%2 == 0):
            answer = answer + '수'
        else:
            answer = answer + '박'
    return answer
    
#소수 찾기
def solution(n):
    all_number = [True]*(n+1)
    m = int((n+1) ** 0.5)
    for i in range(2, m+1):
        if(all_number[i]):
            for j in range(i+i, n+1, i):
                all_number[j] = False
    
    count = 0
    
    for i in range(2, n+1):
        if(all_number[i]):
            count += 1
    
    answer = count
    return answer

#정수 제곱근 판별
import math

def solution(n):
    sqrt = math.sqrt(n)
    if(sqrt.is_integer()):
        return (sqrt+1)**2
    else:
        return -1
    
#2016년
def solution(a, b):
    day = 0
    for i in range(1, a):
        if(i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i== 10 or i ==12):
            day += 31
        elif(i == 2):
            day += 29
        elif(i == 4 or i == 6 or i == 9 or i == 11):
            day += 30
    day += b
    day = day % 7
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[day]

#최댓값과 최솟값
def solution(s):
    s_list = list(map(int, s.split(' ')))
    s_list = sorted(s_list)
    answer = str(s_list[0]) + ' ' + str(s_list[-1])
    return answer

#최솟값 만들기
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer = answer + A[i]*B[i]
        
    return answer

#내적
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

#3진법 뒤집기
def solution(n):
    answer = 0
    ternary = []
    while(n != 0):
        ternary.append(n%3)
        n = n // 3
    for i in range(len(ternary)):
        answer += ternary[i] * (3**(len(ternary)-1-i))
    return answer

#가운데 글자 가져오기
def solution(s):
    middle = len(s) // 2
    if(len(s)%2 == 1):
        answer = s[middle]
    else:
        answer = s[middle-1:middle+1]
    return answer

#같은 숫자는 싫어
def solution(arr):
    answer = []
    for i in arr:
        if(answer):
            if(answer[-1] != i):
                answer.append(i)
        else:
            answer.append(i)
    return answer

#두 정수 사이의 합
def solution(a, b):
    answer = 0
    if(a > b):
        big = a
        small = b
    else:
        big = b
        small = a
    for i in range(small, big+1):
        answer += i
    return answer

#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for i in arr:
        if(i % divisor == 0):
            answer.append(i)
    if(answer):
        answer = sorted(answer)
    else:
        answer.append(-1)
    return answer

#문자열 내 마음대로 정렬하기
def solution(strings, n):
    answer = []
    string_list = []
    strings = sorted(strings)
    for i in strings:
        string_list.append((i[n], i))
    string_list.sort(key = lambda x:x[0])
    for i in string_list:
        answer.append(i[1])
    return answer

#문자열 다루기 기본
def solution(s):
    answer = False
    length = len(s)
    if(length == 4 or length == 6):
        if(s.isdigit()):
            answer = True
    return answer

#서울에서 김서방 찾기
def solution(seoul):
    for i in range(len(seoul)):
        if(seoul[i]=='Kim'):
            index = i
            break
    answer = "김서방은 " + str(index) + "에 있다"
    return answer

#약수의 합
def solution(n):
    answer = 0
    for i in range(n):
        if(n%(i+1) == 0):
            answer += i+1
    return answer

#이상한 문자 만들기
def solution(s):
    answer = ''
    s_list = s.split(' ')
    for word in s_list:
        for i in range(len(word)):
            if(i%2 == 0):
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    answer = answer[:-1]
    return answer

#행렬의 덧셈
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        inner_list = []
        for j in range(len(arr1[i])):
            inner_list.append(arr1[i][j] + arr2[i][j])
        answer.append(inner_list)
    return answer

#x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    answer = []
    number = x
    while(len(answer) != n):
        answer.append(number)
        number = number+x
    return answer

#직사각형 별 찍기
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()
    
#점프와 순간 이동
def solution(n):
    answer = 0
    
    while(n != 0):
        if(n % 2 == 1):
            answer += 1
        n = n // 2

    return answer

#핸드폰 번호 가리기
def solution(phone_number):
    answer = ''
    length = len(phone_number)
    for i in range(length-4):
        answer += '*'
        
    for i in range(length-4, length):
        answer += phone_number[i]
    return answer

#하샤드 수
def solution(x):
    answer = False
    string_x = str(x)
    sum = 0
    for i in string_x:
        sum += int(i)
    if(x % sum == 0):
        answer = True
    return answer

#콜라츠 추측
def solution(num):
    answer = 0
    while(num != 1):
        answer += 1
        if(num % 2 == 0):
            num = num // 2
        else:
            num = num*3 + 1
        if(answer > 500):
            answer = -1
            break
    return answer

#시저 암호
def solution(s, n):
    answer = ''
    print(ord('A'), ord('a'), ord('Z'), ord('z'))
    for i in s:
        if(i == ' '):
            answer += ' '
            continue
        number = ord(i)
        new_number = number + n
        if(number >= 97 and number <= 122):
            if(new_number > 122):
                new_number -= 26
        else:
            if(new_number > 90):
                new_number -= 26
        answer += chr(new_number)
    return answer

#자릿수 더하기
def solution(n):
    answer = 0
    string_number = str(n)
    
    for i in string_number:
        answer += int(i)

    return answer

#자연수 뒤집어 배열로 만들기
def solution(n):
    string_n = str(n)
    answer = list(map(int,string_n))
    answer = list(reversed(answer))
    return answer

#짝수와 홀수
def solution(num):
    if(num % 2 == 0):
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

#정수 내림차순으로 배치하기
def solution(n):
    answer = str(n)
    answer = sorted(answer, reverse=True)
    answer = int(''.join(answer))
    return answer

#제일 작은 수 제거하기
import numpy as np
def solution(arr):
    answer = arr
    if(len(arr) == 1):
        return [-1]
    min = np.min(arr)
    answer.remove(min)
    return answer

#최대공약수와 최소공배수
def solution(n, m):
    if(n > m):
        a = n
        b = m
    else:
        a = m
        b = n
        
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    GDC = a
    LCM = n * m / GDC
    answer = [GDC, LCM]
    return answer

#숫자의 표현
def solution(n):
    answer = 1
    if(n % 2 == 1):
        answer += 1
    for i in range(3, n//2+1):
        if(i % 2 == 1 and n % i == 0):
            answer += 1
    return answer

#이진 변환 반복하기
def solution(s):
    time = 0
    delete = 0
    while(s != '1'):
        time += 1
        count = s.count('1')
        delete += s.count('0')
        s = str(bin(count)[2:])
    answer = [time, delete]
    return answer
