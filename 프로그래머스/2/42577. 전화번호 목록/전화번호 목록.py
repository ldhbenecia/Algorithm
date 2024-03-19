def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        slice_value = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:slice_value]:
            answer = False
            
    return answer
