# 리스트 엘리먼트들의 반복 횟수 구하기
# 두 문자열이 아나그램(Anagrams)인지 확인 가능

# most_common() function 이용 시 리스트에서 가장 많이 반복되는 엘리먼트를 구할 수 있음
# Counter 메서드는 각각의 값들이 몇 개가 있는지 dict() 형태의 타입으로 만들어 줌


# 1번 - 예시 1
# 빼기도 사용 가능
from collections import Counter
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    ans = Counter(participant) - Counter(completion)
    return list(ans)[0]


print(solution(participant, completion))

# output
# mislav


# 1번 - 예시 2
# 리스트의 각 엘리먼트의 반복 횟수 구하기
my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']
count = Counter(my_list)  # COunter 객체 생성

print(count)  # 모든 엘리먼트의 반복 횟수
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b'])  # 특정 엘리먼트의 갯수
# 3

print(count.most_common(1))  # 가장 많이 반복되는 엘리먼트 검색
# [('d', 5)]


# 2번 - 두 문자열이 아나그램인지 확인 = 두 문자열의 Counter 객체가 같으면 아나그램
str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3 = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 and 2 anagram')
if cnt_1 == cnt_3:
    print('1 and 3 anagram')

# output
# 1 and 2 anagram
