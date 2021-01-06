# 첫번째 풀이
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False
    return True


# 두번째 풀이
def solution(phone_book):
    min_value = sorted(list(map(int, phone_book))).pop(0)
    min_value = str(min_value)

    phone_book = [phone[:len(min_value)] for phone in phone_book]

    print('ff', phone_book, min_value)
    if min_value in phone_book[1:]:
        return False
    else:
        return True


# 예진이 참고
def solution(phone_book):
    for x in range(len(phone_book)-1):
         for y in range(x+1,len(phone_book)):
                x_len = len(phone_book[x])
                y_len = len(phone_book[y])
                if x_len <= y_len and phone_book[x] == phone_book[y][:x_len]:
                    return False
                elif phone_book[y] == phone_book[x][:y_len]:
                    return False
    
    return True

