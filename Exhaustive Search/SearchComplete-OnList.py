# 해당 배열 탐색
# 간단한 테크닉이지만 유용한거 같아서 적어둔다.
# for i in range(iterable):
    # print(arr[i + 1]) index 초과 발생

# for i in range(iterable - 1):
    # print(arr[i + 1]) 리스트 안의 index 모두 순회 가능


# 예시
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False
    return True
