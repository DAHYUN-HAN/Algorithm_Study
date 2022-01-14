def solution(phone_book):
    phone_book = sorted(phone_book)
    answer = True
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if(phone_book[i] == phone_book[j][:len(phone_book[i])]):
                answer = False
                return answer
    return answer
