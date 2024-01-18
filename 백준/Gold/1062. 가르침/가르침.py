import sys
from itertools import combinations


# 단어를 비트로 변환
def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord("a"))
    return bit


input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_bit = word2bit("acint")

if K < 5:
    print(0)
else:
    alphabet = [1 << i for i in range(26) if not (base_bit & 1 << i)]  # 학습한 알파벳 모음

    answer = 0
    for combination in combinations(alphabet, K - 5):
        know_bit = sum(combination) | base_bit
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1

        answer = max(answer, count)

    print(answer)

"""
테스트 케이스와 찾아본 반례를 성공했으나,
히든 테스트 케이스의 반례를 못 찾아 다른 사람의 코드를 보고 풀이법을 참고함
"""

# import sys
# from collections import Counter

# input = sys.stdin.readline
# counter = Counter()

# N, K = map(int, input().split())
# total_words_list = []
# for _ in range(N):
#     words = input().strip()

#     # words = words[4 : len(words) - 4]

#     total_words_list.append(words)

#     counter.update(words)


# top_six_alpha_list = []
# for key, vale in counter.most_common(K):
#     top_six_alpha_list.append(key)


# answer = 0
# for string in total_words_list:
#     for char in string:
#         if char not in top_six_alpha_list:
#             break

#     else:
#         answer += 1


# print(answer)

# # top_six_alpha_string = "".join(sorted(top_six_alpha_list))

# # for word in total_words_list:
# #     if word in top_six_alpha_string:
# #         answer += 1

# # print(answer)

# # """
# # 문제 해결 전략
# # 0. 각 특정 단어를 리스트에 담아둔다.
# # 1. Counter를 통해 특정 단어의 알파벳 출몰 상위 6가지를 뽑는다.
# # 2. for 문을 통해 1번에서 나온 6가지의 알파벳이 특정 단어를 모두 충족하는지 하나씩 검증한다.
# # 3. 모두 충족한다면 answer += 1
# # """
