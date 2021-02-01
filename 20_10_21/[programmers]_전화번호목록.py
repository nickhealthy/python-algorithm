# phone_book = ['119', '97674223', '1195524421']
phone_book = ['123', '456', '789']
# phone_book = ['12', '123', '1235', '567', '88']

# 다른 사람 풀이
# def solution(phone_book):
#     phone_book.sort()
#     print(phone_book)
#     for a in range(len(phone_book) - 1):
#         if phone_book[a] in phone_book[a + 1]:
#             return False
#     return True


def solution(phone_book):

    # 정렬을 먼저한다.

    phone_book.sort()

    print(phone_book)

    for idx in range(len(phone_book) - 1):

        # 문자열이 있는지 확인한다 접두어 이기 때문에 문자열을 다 볼 필요는 없다.

        if phone_book[idx] in phone_book[idx + 1][:len(phone_book[idx])]:

            return False

    return True


print(solution(phone_book))